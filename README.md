# Kestra Project Setup and Discord Bot Integration

## Step 1: Install Docker-Compose
1. Install Docker-Compose by following the instructions [here](https://docs.docker.com/compose/install/).

## Step 2: Set Up Kestra
1. Download the Docker Compose file using the following command:
    ```sh
    curl -o docker-compose.yml https://raw.githubusercontent.com/kestra-io/kestra/develop/docker-compose.yml
    ```
2. Navigate to the folder where the `docker-compose.yml` file is located and launch Kestra using:
    ```sh
    docker-compose up -d
    ```
3. Open [http://localhost:8080](http://localhost:8080) in your browser to access the Kestra UI.

For more details, refer to the [Kestra documentation](https://kestra.io/docs/installation/docker-compose#download-the-docker-compose-file).

## Step 3: Create Your Discord Bot
   - Go to Discord settings, click on "Advanced".
   - In the Developer Mode section, click Discord API, then click on Applications.
   - After navigating to [Discord API Applications](https://discord.com/developers/applications), click on "New Application", and name it after your favorite fictional character.
   - Under "Bot", enable all Privileged Gateway Intents and set the permissions to "Administrator".
![Alt text](https://github.com/KaoutharBousbaa1/Kestra_NarutoAI/blob/main/sceenshots/Sreen1.png?raw=true)
![Alt text](https://github.com/KaoutharBousbaa1/Kestra_NarutoAI/blob/main/sceenshots/Screen3.png?raw=true)
   - Save changes and click on "Reset Token" to generate a new token. Copy and save it securely.
![Alt text](https://github.com/KaoutharBousbaa1/Kestra_NarutoAI/blob/main/sceenshots/Nouveau%20projet%20(2).png?raw=true)

## Step 4: Create a Discord Server
1. Create a new Discord server by clicking the "+" button in the Discord app.

## Step 5: Set Up a Webhook
1. In your Discord server, go to server settings, click "Integrations", then "New Webhook". Copy the webhook URL and save it.
![Alt text](https://github.com/KaoutharBousbaa1/Kestra_NarutoAI/blob/main/sceenshots/Nouveau%20projet%20(3).png?raw=true)

## Associate the Webhook to Your Bot

To authorize the Discord bot into your server, follow these steps to generate an OAuth2 link:

1. **Generate the OAuth2 URL:**
    - Under the **"OAuth2 URL Generator"** section, choose **“Bot”** for the scopes.
    - For the bot permissions, choose **“Administrator”**.
    - Scroll down and a generated URL will appear. Copy it and save it somewhere safe.
    - In **General Information**, copy this URL into **“LINKED ROLES VERIFICATION URL”**.

2. **Authorize the Bot:**
    - Go to the **“General Information”** tab.
    - Copy the URL into **“LINKED ROLES VERIFICATION URL”**.
    - Open the URL in a web browser.
    - Select the server you want to add the bot to from the dropdown menu.
    - Click **"Authorize"**.
    - Complete any CAPTCHA challenges if prompted.

## Step 7: Set Up Google Cloud Services
1. Go to the [BigQuery Console](https://console.cloud.google.com/bigquery) and a new dataset.
2. Create tables within the dataset with the required schema here:
    ![Alt text](https://github.com/KaoutharBousbaa1/Kestra_NarutoAI/blob/main/sceenshots/Nouveau%20projet%20(11).png?raw=true)
    ![Alt text](https://github.com/KaoutharBousbaa1/Kestra_NarutoAI/blob/main/sceenshots/Nouveau%20projet%20(12).png?raw=true)
    ![Alt text](https://github.com/KaoutharBousbaa1/Kestra_NarutoAI/blob/main/sceenshots/Nouveau%20projet%20(13).png?raw=true)
    ![Alt text](https://github.com/KaoutharBousbaa1/Kestra_NarutoAI/blob/main/sceenshots/Nouveau%20projet%20(14).png?raw=true)
    ![Alt text](https://github.com/KaoutharBousbaa1/Kestra_NarutoAI/blob/main/sceenshots/Nouveau%20projet%20(15)%20-%20Copie.png?raw=true)
    ![Alt text](https://github.com/KaoutharBousbaa1/Kestra_NarutoAI/blob/main/sceenshots/Nouveau%20projet%20(17)%20-%20Copie.png?raw=true)
   
    Ensure that the tables and schemas match those specified in the YAML code. If you need to add additional tables, ensure that the data types are correct. For this project, you will need the macros, workout,       and steps tables. Refer to the YAML code in the BigQuery task to obtain the correct schema.
4. Create a Google Cloud Storage (GCS) bucket:
   - Navigate to [Google Cloud Console](https://console.cloud.google.com/products/solutions/catalog/?hl=fr).
   - Go to "Resources" -> "Storage" and create a new bucket.

## Step 8: Create and Configure a Service Account
1. Go to the [IAM & Admin Console](https://console.cloud.google.com/iam-admin/iam).
2. After creating the service account, you will see it listed on the Service Accounts page. To manage keys for this service account:

    - On the right side of the service account display name, click `Actions`.
    - Click `Manage Keys`.
    - Click on `Create Key`.
    - The Private Key will now be saved to your computer as a JSON file.
    - Place this file in your Kestra Project directory where the Docker-compose file is located, for better organization.

3. Add to the service account the following roles:
    - BigQuery Admin
    - BigQuery Data Editor
    - BigQuery Data Owner
    - BigQuery Studio Admin
    - BigQuery User
    - Storage Object Admin
    - Storage Object Creator
![Alt text](https://github.com/KaoutharBousbaa1/KestraProject/blob/main/screenshots/Nouveau%20projet%20(9).png?raw=true)

## Step 9: Enable Required APIs
1. Enable the BigQuery API and Google Cloud Storage API in your Google Cloud project:
    - Go to the [API & Services Dashboard](https://console.cloud.google.com/apis/dashboard).
    - Search for "BigQuery API" and "Google Cloud Storage API" and enable them.

## Step 10: Set Up Strava API
1. Create a Strava account [here](https://www.strava.com/register/free?hl=fr-FR).
2. Log in to Strava and create an API application with the Authorization Callback Domain set to `localhost`.
3. Retrieve the Client ID and Client Secret from your Strava API application settings.
![Alt text](https://github.com/KaoutharBousbaa1/KestraProject/blob/main/screenshots/Nouveau%20projet%20(5).png?raw=true)
5. Generate Access and Refresh tokens using Postman or a similar tool:
    - Replace `your_client_id` with your actual client ID in the following URL and paste it into your browser:
      ```sh
      https://www.strava.com/oauth/authorize?client_id=your_client_id&redirect_uri=http://localhost&response_type=code&scope=activity:read_all
      ```
    - You should see a page that looks like this, with your photo and website. Go ahead and hit authorize
   ![Alt text](https://github.com/KaoutharBousbaa1/KestraProject/blob/main/screenshots/Nouveau%20projet%20(7).png?raw=true)
   - After you do that, your browser will probably error. That’s ok. With this error, we actually get the information that we want from Strava. If you look at the navigation bar, the URL should now look like:
      ```sh
      http://localhost/?state=&code=somecode&scope=read,activity:read_all
      ```
      Copy down whatever the code is between code= and the & sign (where my snippet says “somecode”). Now you are ready to get your access and refresh token.
    - You will then make a POST request to Strava which will give you the tokens you need. To make the call in Postman, replace the placeholders in the call below with your Client ID, Client Secret, and the code      from the previous step.

      ```sh
      https://www.strava.com/oauth/token?client_id=your_client_id&client_secret=your_client_secret&code=your_code_from_previous_step&grant_type=authorization_code
      ```
    - Retrieve the Access and Refresh tokens from the JSON response.
      After you make the POST request, you will get a response which includes an Access and Refresh token in the JSON response.
    ![Alt text](https://github.com/KaoutharBousbaa1/KestraProject/blob/main/screenshots/Nouveau%20projet%20(8).png?raw=true)
## Step 11: Encrypt Your Keys
Before proceeding, the Kestra flows interact with external sources such as OpenAI, Google Cloud Storage, BigQuery, Strava API, and Discord. Therefore, it is important to keep your keys secret for practical use.

In our case, in the YAML code, the keys are referenced as `{{ secret('SECRET_KEY_NAME') }}`, while the actual keys are stored in the `.env` file and their encrypted versions in the `.env_encrypted` file.

1. Create an `.env` file in your Kestra project directory with your keys:
    ```sh
    KEY_ONE=THE_ACTUAL_KEY_HERE
    KEY_TWO=THE_ACTUAL_KEY_HERE
    KEY_THREE=THE_ACTUAL_KEY_HERE
    ```
2. Use the following bash script to encode the values:
    ```sh
    while IFS='=' read -r key value; do
        echo "SECRET_$key=$(echo -n "$value" | base64)";
    done < .env > .env_encoded
    ```
3. Update your `docker-compose.yml` file to use the encoded keys:
    ```yaml
    kestra:
      image: kestra/kestra:latest-full
      env_file:
        - .env_encoded
    ```
- Example `.env` file:
    ```sh
    OPENAI_KEY=youropenaikey
    ```
- Example `.env_encoded` file:
    ```sh
    SECRET_OPENAI_KEY=cGFzc3dvcmQHDXEZJHCHKmVJZEVCZECLZEKCLBZKCsnEBLCJLEZJCHCZGELJC
    ```

For more information, refer to the [Kestra Documentation](https://kestra.io/docs/concepts/secret).

## Step 12: Run the Project
1. Navigate to your Kestra project directory containing the `docker-compose.yml` file and runStart Kestra using run Docker Compose:
    ```sh
    docker-compose up -d
    ```
2.  Navigate to your Discord Bot Directory and the command:
    ```sh
    nodemon src/index.js
    ```
3.  Open [http://localhost:8080](http://localhost:8080) in your browser to access the Kestra UI.
4.  Import the flows to Kestra.
   
## Data and Schema Setup
1. Upload the CSV tabes provided here to the daily_macros_demo, totasteps_demo, workout_strava_demo tables in BigQuery
2. In the Discord directory, create an `.env` file with the following code:
    ```sh
    TOKEN=Paste_here_the_token_of_your_discord_bot_from_the_previous_steps
    ```
3. In `index.js`, replace `keyFilename` with your GCS service account key file path and the `projectID` variable with your GCS project ID. Also, replace the `bucketName` variable with the actual bucket name you created in the Google Cloud Storage project:
    ```javascript
    const bucketName = 'your_bucket_name_here';
    ```

## Final Notes
- Ensure that both the Docker Compose setup and the Discord bot are running.
- Remember to configure the timezone in the Kestra UI to fit your local timezone.

Follow these steps, and you'll have your Kestra project and Discord bot up and running smoothly. 
