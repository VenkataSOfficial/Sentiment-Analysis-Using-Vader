# Sentiment-Analysis-Using-Vader
To understand how the reviews and ratings of a product effect the sales of products using concept of NLP
![6387 1532706595](https://user-images.githubusercontent.com/77020328/116319321-51831980-a784-11eb-86a2-46f8a26a033b.png)
For this project first of all I started with downloading the reviews and ratings of the 10 best selling smartphone brands on Amazon

To aggregrate this data into an Excel sheet we use Amazon product data API using which we can download the reviews into an Excel sheet.

For sentiment analysis we used the VADER model from the NLTK library which basically provides the scores based on a few factors such as words used, capitalization, punctuations and negotiations.

For doing analysis I had to use the sentiment intensity analyzer function from the Vader module and simply made an object of the Vader module class to access the sentiment intensity analyzer function, which we will use to label the statement as either positive negative or neutral.

Basically each statement from a review would be checked for the polarity and then rated on three categories how negative the statement is, how positive the statement is and how neutral the statement is.

Then we simply aggregated all the three scores into a compound score by normalizing them.

The over all accuracy I got by comparing the labels from  Amazon to the compounds course is of 70.98% or almost 71% accuracy.
