# CSV Data Analysis and Visualization
This Django web application allows users to upload CSV files, analyze the data using pandas and NumPy, and visualize the results on the web interface.

+ Uploads CSV files and parses them using pandas.
+ Performs basic data analysis like calculating descriptive statistics.
+ Generates visualizations like histograms for numerical columns using matplotlib.
+ Displays the analysis results and visualizations on a user-friendly web page.



### Setup instructions
1. Create a Virtual Environment `python -m venv django`
2. Activate the Virtual Environment `source django/bin/activate`
4. Clone the repository `git clone https://github.com/ycisir/ve3_task.git`
5. Install dependencies `cd ve3_task` then `pip install -r requirements.txt`
6. Run the Django development server `python manage.py runserver`

> [!NOTE]
> Make sure run the `python manage.py makemigrations` and `python manage.py migrate` command before run the server.
