SELECT CART_ID
FROM CART_PRODUCTS CT1
WHERE NAME = 'Milk'
    AND CART_ID IN (SELECT DISTINCT(CART_ID)
                   FROM CART_PRODUCTS CT2
                   WHERE NAME = 'Yogurt') 
ORDER BY ID ASC ;

