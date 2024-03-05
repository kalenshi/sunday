SELECT
    `payment`.`payment_id`,
    `payment`.`customer_id`,
    `payment`.`staff_id`,
    `payment`.`rental_id`,
    `payment`.`amount`,
    `payment`.`payment_date`,
    `payment`.`last_update`
FROM `payment`
    WHERE 1=1
     AND `payment`.`payment_id` = 259
