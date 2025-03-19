# Scenario-2-Containerizing-the-Star-Wars-API-Scanner

# Task:

**Containerize the Star Wars API Scanner script (from Scenario 1) using Alpine Linux as the base image.**

**Requirements:**

✅ Use Alpine Linux as the base image

✅ Publish the Docker image on Docker Hub for testing

✅ Store the Dockerfile and related code in a GitHub repository

**📌 Prerequisites**
Before running the container, ensure you have Docker installed on your system.

```bash
$ sudo apt update
```

```bash
$ sudo apt install docker.io
```
```bash
$ sudo usermod -aG docker ubuntu
```

**📥 Clone the Repository**

```bash
$ git clone https://github.com/vijayrajuyj1/Scenario-2-Containerizing-the-Star-Wars-API-Scanner.git
```

**🏗 Build the Docker Image**

Run the following command to build the Docker image:

```bash
$ docker build -t vijayarajult2/swapi:v1 .
```

**🚀 Run the Docker Container**
```bash
$ docker run vijayarajult2/swapi:v1
```

**📌 Note: Ensure you have an active internet connection for API calls.**

**Push that docker image to your Dockerhub**

**Docker Hub Link:**
Provide the published container image URL: vijayarajult2/swapi:v1

Now, to pull and run this image, others can use the following commands:

```bash
docker pull vijayarajult2/swapi:v1
```

```bash
docker run  vijayarajult2/swapi:v1
```

**📜 Expected Output (JSON Format)**
```json
{
    "film": "A new Hope",
    "starships": [
        {
            "starship": "CR90 corvette",
            "pilots": []
        },
        {
            "starship": "Star Destroyer",
            "pilots": []
        },
        {
            "starship": "Sentinel-class landing craft",
            "pilots": []
        },
        {
            "starship": "Death Star",
            "pilots": []
        },
        {
            "starship": "Millennium Falcon",
            "pilots": [
                "Chewbacca",
                "Han Solo",
                "Lando Calrissian",
                "Nien Nunb"
            ]
        },
        {
            "starship": "Y-wing",
            "pilots": []
        },
        {
            "starship": "X-wing",
            "pilots": [
                "Luke Skywalker",
                "Biggs Darklighter",
                "Wedge Antilles",
                "Jek Tono Porkins"
            ]
        },
        {
            "starship": "TIE Advanced x1",
            "pilots": [
                "Darth Vader"
            ]
        }
    ]
}
```


**🛠 Built With**

✅ Python 3 – Fetching API data

✅ Docker – Containerization

✅ Alpine Linux – Lightweight base image


---

### 📩 Contact

**Vijayaraju DevOps and Cloud Engineer**  
📧 Email: [vijayaraju7360@gmail.com](mailto:vijayaraju7360@gmail.com)
