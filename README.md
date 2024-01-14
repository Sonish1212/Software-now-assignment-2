Question one contains multiple csv files with large text which has to be handled using NLP (Natural Language Processing).
In task-1 all those CSV files data has to be stored in a single text file.
<img width="1196" alt="Screenshot 2024-01-09 at 12 59 45 PM" src="https://github.com/Sonish1212/Software-now-assignment-2/assets/69333078/a4fe0a6b-5842-41a0-a104-6852490423e4">
Here using pandas library all the csv files were read and stored as a text file in all_csv_file.txt


In Task-2 from the text file we get from task-1 top 30 words were extracted and were counted.


<img width="1102" alt="Screenshot 2024-01-09 at 1 07 47 PM" src="https://github.com/Sonish1212/Software-now-assignment-2/assets/69333078/ba623df9-f5c6-4fe5-9958-1a0fc2091814">
Here a function was created to open the file and to process the text in file after that to find the top 30 repeated words and to store those words in a csv file using the csv library.
At the end the function was call and the parameters were inserted to get the final top 30 words from the text file.


In Task-4 there we have to compare two of the models for finding the drugs and disease entities from the huge text file. While running the both code i understand about tthe proessing speed of both of the models. 
While using biobert which is basically a model that is specially used for the extraction of medical words and entites the processing was much faster and the memory usage was a bit less than en_core_sci_sm.
While using biobert i find the result as follows:

<img width="1388" alt="Screenshot 2024-01-14 at 2 05 30 PM" src="https://github.com/Sonish1212/Software-now-assignment-2/assets/69333078/1674b82f-879b-43c8-a93e-f7da4c8b5e80">

But while using the en_core_sci_sm the processing was too slow and there was problem with the memory usage after using cprofile, batch and chunks for processing the text much faster the computer memory couldnot hold and it always ends up saying killed:9

