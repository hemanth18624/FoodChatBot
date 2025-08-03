# Food Order ChatBot 🍔🤖

A sophisticated and interactive chatbot agent designed to streamline the food ordering process. This bot, built with **Google Dialogflow** for Natural Language Understanding (NLU) and a powerful **FastAPI** backend, allows users to place, modify, and track their food orders seamlessly.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green.svg)
![SQL](https://img.shields.io/badge/Database-SQL-orange.svg)
![Dialogflow](https://img.shields.io/badge/Dialogflow-ES-yellow.svg)

---

## 🎯 Core Features

This chatbot provides a complete and user-friendly food ordering experience with the following key capabilities:

* **Place a New Order:** Users can conversationally browse the menu and place a new food order.
* **Modify an Existing Order:** Before an order is finalized, users can easily add more items or remove existing ones from their cart.
* **Track Order Status:** Users can get real-time updates on the status of their order, from preparation to delivery.

---

## 🏗️ Architecture & Tech Stack

The project leverages a modern, high-performance tech stack to ensure a responsive and reliable user experience.

* **Natural Language Understanding (NLU):** **Google Dialogflow** is used to design the conversational experience.
    * **Intents:** Define the user's intention (e.g., `order_add`, `order_complete`, `order_track`,`order_remove`).
    * **Entities:** Extract key information from user input (e.g., `food_item`, `quantity`, `order_id`).
    * **Contexts:** Manage the flow of conversation and maintain state.

* **Backend Service:** **FastAPI**, a high-performance Python web framework, serves as the webhook fulfillment service. It handles all the business logic, database interactions, and response generation.

* **Database:** A **SQL Database** MySQL is used for persistent data storage.
    * **`FoodItems` Table:** Stores menu item details and prices.
    * **`Orders` Table:** Stores the contents and details of each order.
    * **`OrderTracking` Table:** Maintains the real-time status of each order.

### Workflow Diagram

The interaction flow is designed for efficiency and real-time feedback.
1.  The user sends a message to the chatbot.
2.  **Dialogflow** processes the natural language, identifies the intent, and extracts entities.
3.  Dialogflow sends a webhook request to the **FastAPI** backend with the parsed data.
4.  The FastAPI application executes the required business logic (e.g., creating, updating, or querying an order).
5.  The backend interacts with the **SQL database** to persist or retrieve data.
6.  A JSON response is formulated and sent back to Dialogflow.
7.  Dialogflow delivers the final text response to the user.

---

## Demo

https://youtu.be/VVB-A4lfVFA?si=fjPMcOC9OCiZY9Mz
https://youtu.be/OqSZzACJQj0?si=SVCkCR1PTNafEbjJ
https://youtu.be/Qp5JMR0htXU?si=m286igwWMLv4yicj

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

* Python 3.1+
* A Google Cloud Platform account with the Dialogflow API enabled
* `ngrok` or a similar tool to expose your local server to the internet.

### Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/hemanth18624/FoodChatBot.git](https://github.com/hemanth18624/FoodChatBot.git)
    cd FoodChatBot
    ```

2.  **Set Up a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Configuration**
    * Set up your SQL database.
    * Configure the database connection string in your environment variables or a configuration file (e.g., `.env`).

5.  **Run the Backend Server**
    ```bash
    uvicorn main:app --reload
    ```
    The server will be running on `http://127.0.0.1:8000`.

### Dialogflow Configuration

1.  **Create/Import Agent:**
    * Go to the [Dialogflow Console](https://dialogflow.cloud.google.com/).
    * Create a new agent or import the provided `agent.zip` file (if available in the repository).

2.  **Enable Webhook Fulfillment:**
    * In your Dialogflow agent's settings, navigate to the **Fulfillment** section.
    * Enable the **Webhook**.
    * Expose your local server using `ngrok`:
        ```bash
        ngrok http 8000
        ```
    * Copy the HTTPS URL provided by `ngrok` and paste it into the **URL** field in Dialogflow's fulfillment settings. Add the appropriate webhook endpoint path (e.g., `https://your-ngrok-url.io/webhook`).
    * Save your changes.

3.  **Enable Webhook for Intents:**
    * For each intent that requires backend logic (`order.place`, `order.modify`, etc.), scroll down to the **Fulfillment** section within the intent configuration and toggle on **"Enable webhook call for this intent"**.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request for any improvements or bug fixes.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---


[Watch Demo Video](demo1.mp4)


## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
