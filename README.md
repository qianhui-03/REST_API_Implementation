# REST_API_Implementation
## Overview
This project demonstrates how to build a simple REST API using **Flask** and **Flask-RESTful** in Python.

## Objectives
1. Understand how REST APIs work using Flask.
2. Compare standard Flask routing with Flask-RESTful.
3. Learn GET vs POST.
4. Return JSON responses.
5. Test APIs using Postman.

## Methodology
1. Create a Flask application.
2. Define API routines using `@app.route` with **GET** and **POST** methods.
3. Implement logic inside route functions.
4. Return results in JSON format using `jsonify`.
5. Test the API with **Postman** or a browser.

## Key Takeaways
- Flask provides a way to create REST APIs.
- **GET** requests are ideal for quick retrievals.
- **POST** requests allow sending structured data, which is better for complex operations or sensitive inputs.
- Testing APIs in Postman helps verify server logic before building a frontend.

## Why it matters
- REST APIs are fundamental to modern applications, data pipelines and web services.

## Tech Stack
- Python 3.13.0
- Flask
- Postman

## Project Structure
```
├── README.md
├── REST_API_Flask.py
├── REST_API_Flask-RESTFUL.py
```

## Installation
1. Clone the repo and install dependencies:

    ```bash
    git clone https://github.com/qianhui-03/REST_API_Implementation.git
    cd REST_API_Implementation
    pip install flask flask-restful
    ```

2. Run the server.
3. Test endpoints in Postman or browser.

# Visual Map of Routes
```bash
API Server (http://127.0.0.1:5000)
│
├── Flask @app.route Endpoints:
│   ├── GET /               → home()
│   │     Returns: {"data": "hello world"}
│   │
│   ├── GET /square/<num>   → disp(num)
│   │     Example: /square/5 → {"result": 25}
│   │
│   └── POST /square        → square_post()
│         Body: {"num":5} → {"square": 25}
│
├── Flask-RESTful Class Endpoints:
│   ├── GET /               → Hello.get()
│   │     Returns: {"message": "hello world"}
│   │
│   ├── GET /square/<num>   → Square.get(num)
│   │      Example: /square/5 → {"square": 25}
│   │
│   └── POST /cube           → CubePost.post()
│          Body: {"num":2} → {"cube": 8}
```
## References
- <a href="https://www.geeksforgeeks.org/python/python-build-a-rest-api-using-flask/ " target="_blank">
  GeeksforGeeks: Python - Build a REST API using Flask
</a>
