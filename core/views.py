from django.shortcuts import render, redirect
from .forms import UploadCSVForm
from .models import UploadedCSV
from django.contrib import messages
import pandas as pd
import csv, codecs
import numpy as np
import matplotlib.pyplot as plt
import os


def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)

        if form.is_valid():
            uploaded_file = form.cleaned_data['csv_file']
            # print(uploaded_file)
            messages.success(request, 'File uploaded successfully!')
            
            with uploaded_file.open('rb') as csv_data:
                data = pd.read_csv(csv_data)

                # to show data on webpage
                top = data.head(7)

                # for all int type values
                # df_int = data.select_dtypes(include=['int64', 'float64'])
                # mean = df_int.mean()
                # median = df_int.median()
                # # sum = df_int.sum()
                # sd = df_int.std()
                # nv = (data.isna().sum())
                # statistics = {'mean':mean, 'median':median, 'sd':sd, 'nv':nv}

                # for single column
                mean = data['Salary'].mean()
                median = data['Salary'].median()
                # sum = data['Salary'].sum()
                sd = data['Salary'].std()
                nv = (data['Salary'].isnull().sum())
                statistics = {'mean':mean, 'median':median, 'sd':sd, 'nv':nv}

                # filling null values with previous one
                # data = data.fillna(method ='pad')

                # filling null values with mean value
                data['Salary'].replace([np.nan], data['Salary'].median(), inplace=True)
                data['Salary'].apply(np.ceil)
                print(data.head())

                data.hist(column='Salary',edgecolor='black')
                plt.title('Histogram of Salary Data')
                plt.xlabel('Salary')
                plt.ylabel('Experience')
                save_results_to = '/home/yasir/Documents/projects/django/ve3_task/core/static/core/images/'
                plt.savefig(save_results_to + 'hist.png', dpi = 300)

            return render(request, 'core/dashboard.html', {'columns': data.columns, 'rows': top.to_dict('records'), 'statistics':statistics})
    else:
        form = UploadCSVForm()
    return render(request, 'core/index.html', {'form': form})
