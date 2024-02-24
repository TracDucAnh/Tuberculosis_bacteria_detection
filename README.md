# Tuberculosis bacteria detection using YOLOv8

## Breif summary of tuberculosis

According to WHO (World Health Oranization), Tuberculosis (TB) also known colloquially as the "white death", is an infectious disease that most often affects the lungs and is caused by a type of bacteria, Mycobacterium tuberculosis (a species of pathogenic bacteria in the family Mycobacteriaceae and the causative agent of tuberculosis). First discovered in 1882 by Robert Koch, about a quarter of the global population is estimated to have been infected with TB bacteria. About 5–10% of people infected with TB will eventually get symptoms and develop TB disease.

A total of 1.3 million people died from TB in 2022 (including 167 000 people with HIV). Worldwide, TB is the second leading infectious killer after COVID-19 (above HIV and AIDS).

In 2022, an estimated 10.6 million people fell ill with tuberculosis (TB) worldwide, including 5.8 million men, 3.5 million women and 1.3 million children. TB is present in all countries and age groups. TB is curable and preventable.

In the scope of computer science and data science, this bacteria sample could be trainable data to develop deep learning models to detect bacteria from images with highly accurate results. Images of the bacteria could be conveniently collected through the microscope with the patient's sputum sample.

## Brief summary of the project

This project was conducted to apply a deep learning model (CNN) to detect bacteria from a given image of a patient's sputum. The aim of this project was to find an effective way to detect all the bacteria that exist in the image accurately.

The project has been through 2 periods of time. First, the previous approach was trying to crop some region samples of bacteria and environments from training images to feed the CNN model. Through the training process, the CNN model could classify a particular region from an image containing tuberculosis bacteria or not. But this approach proved to be cumbersome, it was calculation-expensive,

## Why YOLOv8 suitable for image detection tasks?

## The latest work on this TB detection project and the previous approaches using CNN to classify and then localize the bacteria coordinates prove cumbersome