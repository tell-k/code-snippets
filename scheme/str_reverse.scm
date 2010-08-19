(define (list-reverse ls)
 (letrec
  ((rev (lambda (ret l)
         (if (null? l)
          ret
          (rev (cons (car l) ret)
           (cdr l))))))
  (rev '() ls)))
(define (str_reverse str)
    (list->string (list-reverse (string->list str))))
(print (str_reverse "あいうえお日本語"))
