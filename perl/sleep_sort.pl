#!perl
use strict;
use warnings;
use Time::HiRes qw(sleep);
use IO::Select;

use Data::Dumper;

sub sleep_sort {
    my @input = @_;
    my @output;
    my $watcher = IO::Select->new();
    my @children;

    foreach my $value(@input) {
        my $pid = open my $io, '-|';
        defined($pid) or die $!;

        if($pid == 0) {
            sleep $value / 10;
            print $value;
            exit;
        }
        else {
            $watcher->add($io);
            push @children, $pid;
        }
    }

    while($watcher->count > 0) {
        foreach my $io( $watcher->can_read(0) ) {
            $watcher->remove($io);
            push @output, <$io>;
            close $io;
        }
    }

    waitpid $_, 0 for @children;

    return @output;
}

print Dumper([ sleep_sort @ARGV ]);
__END__
$ perl sleep-sort.pl 1 3 5 2 4
$VAR1 = [
'1',
    '2',
    '3',
    '4',
    '5'
    ];
