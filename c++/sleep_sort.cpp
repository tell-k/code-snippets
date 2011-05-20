//http://d.hatena.ne.jp/wordi/20110519/p1

#include <Windows.h>
#include <iostream>

#include <boost/thread/thread.hpp>
#include <boost/thread/mutex.hpp>
#include <boost/bind/bind.hpp>

boost::mutex m;

void func(int n)
{
    Sleep(n * 1000);

    m.lock();
    std::cout << n << " ";
    m.unlock();
}

int main()
{
    int a[] = {3, 1, 8, 7, 2, 4, 9, 6, 0, 5};
    int n = sizeof(a) / sizeof(a[0]);

    boost::thread_group group;

    for (int i = 0; i < n; ++i)
        group.create_thread(boost::bind(func, a[i]));

    group.join_all();

    return 0;
}
