# n8n Workflows for Content Moderation

This project contains n8n workflows designed for content moderation, specifically for User-Generated Content (UGC). The workflows handle PII (Personally Identifiable Information) detection, image censoring, and administrator notifications.

The solution is built using a combination of FastAPI as the backend and leverages various Upstage APIs for advanced AI capabilities.

## Workflows

The core workflows implemented in this project are:

1.  **UGC PII Detection:** Analyzes text content to identify and flag any personally identifiable information.
2.  **Image Censoring:** Processes images to detect and censor inappropriate content, including face detection.
3.  **Admin Notification:** Automatically notifies administrators when content is flagged for PII or inappropriate imagery.

## Workflow Architecture

This project includes two main workflow models, as illustrated below.

### Model 1

Model 1 is a service that identifies personal information before uploading images for marketing purposes. It detects whether a face is present in the image and whether the text within the image contains any personal information, and then provides a notification.

![Model 1](n8n/Model%201.png)

### Model 2

Model 2 has two main functions:

1.  **Periodic UGC Collection & Filtering:** It periodically collects User-Generated Content (UGC) from social media. If the UGC contains sensitive information (e.g., faces, personal data), it is excluded from the collection. The collected UGC is then used to build a Retrieval-Augmented Generation (RAG) system using Upstage's Embedding API.

2.  **Chat-Based UGC Querying:** An Agent AI is built using the collected UGC data and powered by Upstage's Solar Pro 2 LLM. This enables users to query the UGC information through a chat-based interface.

![Model 2](n8n/Model%202.png)


## Project Structure

Here is an overview of the project's folder structure:

```
ai-agent-hackathon-api/
├── app/
│   ├── main.py                # Main FastAPI application
│   ├── controllers/
│   │   └── image_controller.py
│   ├── routes/
│   │   └── image_route.py
│   └── services/
│       └── image_service.py
├── n8n/                       # n8n workflow files and diagrams
│   ├── Model 1.json
│   └── Model 2.json
├── .gitignore
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Requirements

To run this project, you will need the following:
- API Keys for:
  - Upstage
  - X (Twitter)
- WebHook URL for Discord notifications
- Server with:
    - n8n
    - FastAPI
    - Redis

## Getting Started

### Running the Backend Server

To run the backend server, use the following command:

```bash
uv run fastapi run
```

## Technologies Used

*   n8n
*   FastAPI
*   OpenCV
*   RAG
*   Redis
*   Upstage AI APIs
    *   Solar Pro 2
    *   Document parsing
    *   Embeddings

## Hackathon

This project was developed for the Pusan National University x Upstage AI Agent Hackathon.

- **Event:** Pusan National University x Upstage AI Agent Hackathon
- **Date:** 2025.11.12 - 2025.11.19
- **Link:** [https://cse.pusan.ac.kr/cse/14651/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGY3NlJTJGMjYwNSUyRjE3NDU2MzIlMkZhcnRjbFZpZXcuZG8lM0ZiYnNPcGVuV3JkU2VxJTNEJTI2aXNWaWV3TWluZSUzRGZhbHNlJTI2c3JjaENvbHVtbiUzRCUyNnBhZ2UlM0Q1JTI2c3JjaFdyZCUzRCUyNnJnc0JnbmRlU3RyJTNEJTI2YmJzQ2xTZXElM0QlMjZwYXNzd29yZCUzRCUyNnJnc0VuZGRlU3RyJTNEJTI2](https://cse.pusan.ac.kr/cse/14651/subview.do?enc=Zm5jdDF8QEB8JTJGYmJzJTJGY3NlJTJGMjYwNSUyRjE3NDU2MzIlMkZhcnRjbFZpZXcuZG8lM0ZiYnNPcGVuV3JkU2VxJTNEJTI2aXNWaWV3TWluZSUzRGZhbHNlJTI2c3JjaENvbHVtbiUzRCUyNnBhZ2UlM0Q1JTI2c3JjaFdyZCUzRCUyNnJnc0JnbmRlU3RyJTNEJTI2YmJzQ2xTZXElM0QlMjZwYXNzd29yZCUzRCUyNnJnc0VuZGRlU3RyJTNEJTI2)
