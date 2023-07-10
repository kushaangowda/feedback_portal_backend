# Customer Feedback Portal (Backend)

Welcome to Customer Feedback Portal!!!

This platform serves as a testing ground for the APIs we have developed, aimed at simplifying the analysis of customer feedback.

Try it [here](https://master--feedback-portal.netlify.app).

You can find the frontend repository [here](https://github.com/kushaangowda/feedback_portal).

## Prompt

Build an API endpoint that integrates an LLM (either GPT or an open-source model from Hugging Face). We’re looking for exciting solutions to real-world problems. (Track 2 of Mercor Hackathon)

## Features

1. Our API leverages the DaVinci model, developed by openAI, to address customer issues encountered while analyzing feedback for a specific product. This model, known for its lightweight design, plays a crucial role in generating a concise summary that encompasses both positive and negative responses. By condensing the feedback into a summary, we can easily grasp the overall sentiment and identify key points without having to go through lengthy reviews.
2. Additionally, our API goes beyond generating a summary by providing appropriate replies to customers based on their feedback. This feature ensures that customers receive timely and personalized responses, fostering a sense of engagement and satisfaction.
3. Moreover, by considering all the received reviews, our API compiles a comprehensive set of positive and negative responses, including the average product rating. This compilation helps customers in making informed decisions as they can quickly assess the overall sentiment and gauge the general satisfaction level of other users. It also saves time by providing a consolidated view of feedback, eliminating the need to individually analyze numerous reviews.
4. In summary, these features collectively enhance the customer experience by simplifying the analysis of feedback, empowering customers with a clear overview, and facilitating prompt and tailored responses. Ultimately, this automated approach helps in effectively resolving customer issues and improving overall satisfaction.

## Playground Components

1. Overall Insight: Creates a comprehensive perspective by consolidating the entirety of the customer review database
2. Reviews: Compilation of reviews, encompassing their respective positive and negative feedback, accompanied by appropriate customer replies.
3. Add Review: A module designed for incorporating fresh reviews

## Technologies Used

1. FrontEnd: ReactJS
2. Backend: Flask, OpenAI API
3. Database: MongoDB

## Installation

1. Clone the repository
2. Install the requirements `$ pip install -r requirements.txt`
3. Create a .env file with the following keys: OPEN_API_KEY, MONGO_URI
4. Start the server `$ flask --app server run`

## References

1. Reviews dataset from Kaggle: [https://www.kaggle.com/datasets/parve05/customer-review-dataset?resource=download](https://www.kaggle.com/datasets/parve05/customer-review-dataset?resource=download)
2. Open AI API: [https://openai.com/blog/openai-api](https://openai.com/blog/openai-api)
