;フィボナッチ数列

(define (fib n)
 (if (or (zero? n)(= n 1))
     1
     (+ (fib (- n 1))
        (fib (- n 2)))))

(print (fib 1)) ;=> 1
(print (fib 0)) ;=> 1
(print (fib 2)) ;=> 2
(print (fib 3)) ;=> 3
(print (fib 4)) ;=> 5
