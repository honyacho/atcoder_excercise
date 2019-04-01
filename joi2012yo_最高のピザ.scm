(define num-topping (string->number (read-line)))
(define num-pair (map 
  string->number
  (string-split (read-line) " ")
))
(define price-base (car num-pair))
(define price-top (car (cdr num-pair)))
(define cal-base (string->number (read-line)))

(define top-cals (sort 
  (let loop ((n1 1) (now '()))
    (if (> n1 num-topping)           
      now
      (let ((m (+ n1 1)))
        (loop m (cons (string->number (read-line)) now))
      )))
  >
))

(define result (let loop 
  ((lst top-cals)
   (cal cal-base)
   (price price-base))
  (if (null? lst)
    (print (floor (/ cal price)))
    (let
      ((next-cal (+ cal (car lst))) 
       (next-price (+ price price-top)))
      (if (> (/ next-cal next-price) (/ cal price))
        (loop (cdr lst) next-cal next-price)
        (print (floor (/ cal price)))
      ))
  )
))