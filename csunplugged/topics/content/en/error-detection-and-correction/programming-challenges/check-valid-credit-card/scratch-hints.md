-   Every second number (the odd digits of the credit card, i.e. 1st, 3rd,
    5th, and so on digits) is multiplied by 2, but if this gives a 2-digit
    number you should subtract 9 from it.
    For example, if the input digit 8 is multiplied by 2, that gives 16,
    and subtracting 9 from that gives 7 to add to the running total
    (some descriptions of the method say that you should add the two digits
    together, which gives the same result e.g. for 8x2 = 16 adding the digits
    in the result is 1+6, which is also 7).

-   You then add the sum of these values to the sum of the even digits of the
    credit card.
    The credit card number is valid if the final total is a multiple of 10
    (i.e. total mod 10 is equal to 0).
