SELECT COLUMN_NAME, 
       COLUMN_TYPE, 
       IS_NULLABLE, 
       COLUMN_DEFAULT, 
       EXTRA
FROM information_schema.columns
WHERE table_schema = 'alx_book_store' 
  AND table_name = 'books';
