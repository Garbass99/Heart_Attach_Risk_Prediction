# Heart_Attach_Risk_Prediction
This Application is designed to predict the risk of developing heart attack among individuals and provide further guidiance
<img width="1808" height="785" alt="image" src="https://github.com/user-attachments/assets/c8d37646-24b8-4fc3-bb93-57da50e6d2ec" />
Clinical Variables & Measurement Instruments for Heart Attack Prediction
link to Model deploy to streamlit: https://garbass99-heart-attach-risk-prediction-app-sc7q4i.streamlit.app/

Variable (Code Name) | Clinical Meaning | How It's Measured (Clinical Instruments & Tests) 
1.  Age | Verified via patient history (ID, verbal confirmation).
2. sex` | Biological Sex | Verified via patient history.
3. `cp` (Chest Pain Type) | Type of Chest Pain | Assessed through patient history and interview by a physician. The description of the pain (location, quality, radiation, duration, triggers) is crucial for classification. |
4. `trestbps` (Resting BP) | Resting Blood Pressure | Measured using a sphygmomanometer (manual blood pressure cuff) or an automated digital blood pressure monitor. Patient must be seated and at rest for at least 5 minutes. |
5. `chol` (Cholesterol) | Serum Cholesterol | Measured via a blood test (often a lipid panel or lipid profile). A sample of blood is drawn from the patient's vein and analyzed in a laboratory. |
6. `fbs` (Fasting Blood Sugar) | Fasting Blood Sugar | Measured via a fasting blood glucose test. A blood sample is taken after the patient has fasted (not eaten) for at least 8 hours. |
7. `restecg` | Resting Electrocardiogram | Measured using an electrocardiogram (ECG or EKG) machine**. Electrodes are placed on the patient's chest, arms, and legs to record the heart's electrical activity at rest. |
8. `thalach` (Max HR) | Maximum Heart Rate Achieved | Measured during a Cardiac Stress Test (Treadmill Test or Exercise ECG). The patient exercises on a treadmill or stationary bike while connected to an ECG machine. Heart rate is monitored until peak exertion is reached. |
9. `exang` | Exercise-Induced Angina | Observed and reported during the Cardiac Stress Test. The physician or technician asks the patient if they are experiencing chest pain during the exercise. |
10. `oldpeak` | ST Depression | Measured from the ECG results during the Cardiac Stress Test. The software on the ECG machine automatically calculates the deviation (depression) of the ST segment from the baseline, which indicates heart muscle stress. |
11. `slope` | Slope of Peak ST Segment | Analyzed by a cardiologist from the ECG tracings during the peak of the stress test. It is a visual interpretation of the shape of the ST segment. |
12. `ca` | Number of Major Vessels | Visualized and counted via Coronary Angiography (Cardiac Catheterization). A catheter is threaded into the heart's arteries, a contrast dye is injected, and X-ray fluoroscopy is used to see blockages and count affected vessels. |
13. `thal` | Thallium Scan Result / Blood Flow | Determined by a Thallium Stress Test (Nuclear Stress Test). A radioactive tracer (Thallium) is injected into the bloodstream. A gamma camera then takes images of the heart at rest and after stress to show areas with poor blood flow.

