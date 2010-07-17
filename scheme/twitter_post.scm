;synopsis 
; Twitterにポスト
;
; gosh twitter_post.scm username password "message"
;
;ref 
; http://my-snippet.appspot.com/snippet/show/8019
;

(use rfc.http) ; http-post
(use rfc.uri) ; uri-encode-string
(use rfc.base64) ; base64-encode-string

(define *twitter-status* "/statuses/update.xml?status=")
(define *twitter* "twitter.com")

(define make-authorization
  (lambda (username password)
    (string-append "Basic "
                   (base64-encode-string
                     (string-append username ":" password)))))

(define make-poster
  (lambda (base-host post-path)
    (lambda (auth)
      (lambda (message)
        (http-post base-host
                   (string-append post-path
                                  (uri-encode-string message))
                   ""
                   :authorization auth)))))

(define main
  (lambda (args)
    (((make-poster *twitter* *twitter-status*)
      (make-authorization (cadr args)(caddr args))) (cadddr args))))


