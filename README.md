# palm oil spot
Using docker, airflow postgresql and sklearn for this project to forecast palm oil spot price for 3 months 

Steps To Run and View Results on Airflow:
This is tested successfuly on linux ubuntu os.
1. In terminal, change the active directory to the folder that contains the docker-compose.yml

2. In terminal, run 'docker-compose build'

3. In terminal, run 'docker-compose up'

4. To view airflow webui, open your browser to localhost:8080
![image](https://user-images.githubusercontent.com/36352341/80977932-ff046b00-8e57-11ea-9b7e-a41c00e6688a.png)

5. Trigger the task manually to run.
![image](https://user-images.githubusercontent.com/36352341/80977795-cf556300-8e57-11ea-9cc6-8f125f6018fa.png)

6. Click on Dag id
![image](https://user-images.githubusercontent.com/36352341/80978790-1b54d780-8e59-11ea-8b1d-0e0173caf7b9.png)

7. Click on Graph View
![image](https://user-images.githubusercontent.com/36352341/80978867-358eb580-8e59-11ea-8791-c24732cbde87.png)

8. Click on get_forecast
![image](https://user-images.githubusercontent.com/36352341/80978952-4f2ffd00-8e59-11ea-9afa-c8c5aeb806dc.png)

9. Click on XCom
![image](https://user-images.githubusercontent.com/36352341/80979018-640c9080-8e59-11ea-8aed-3e9a8d732dc8.png)

10. The results from model forecasting is displayed
![image](https://user-images.githubusercontent.com/36352341/80979098-7f779b80-8e59-11ea-8587-042881b3babb.png)
