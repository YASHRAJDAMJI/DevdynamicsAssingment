# Devdynamics Assignment
Worked on the **1st problem statement (Publisher Subscriber Notification System)**

### Links
- **Postman Workspace:** [Link to Postman Workspace](https://www.postman.com/aerospace-geoscientist-54538886/workspace/my-workspace/collection/36249673-423bdde7-ea20-4f66-a894-5f4d3ad76dbf?action=share&creator=36249673)
- **Import collection by this link:** [Import Collection](https://api.postman.com/collections/36249673-423bdde7-ea20-4f66-a894-5f4d3ad76dbf?access_key=PMAT-01J04A7QV1JKCBXAB7ER2RF24Y)
- **Website link (Base URL):** [https://yashraj22.pythonanywhere.com/](https://yashraj22.pythonanywhere.com/)

### API Endpoints
In this assignment, I created the following APIs for the Publisher Subscriber Notification System:

1. **createsubscriberid ("name"):** 
   - This API will create a unique alphanumeric ID of 6 characters.
   - Ensures secure handling of users uniquely.
   - Takes the input as the name.

2. **getsubscriberid ("name"):**
   - This API will return the unique API ID created by the `createsubscriberid` API.
   - Takes the input as the name of the user.
   - Helps to get the Subscriber ID of a user by name if the user is already registered.

3. **subscribe ("topicId", "subscriberId"):**
   - This API allows a user to subscribe to a topic.
   - Takes input as `topicId` and `subscriberId`.

4. **notify ("topicId"):**
   - This API retrieves all subscribers who are subscribed to a particular topic.

5. **unsubscribe ("topicId", "subscriberId"):**
   - This API allows a user to unsubscribe from a particular topic.

### API Flow
The recommended flow for using the APIs is as follows:

1. **Create Subscriber ID:**
   - Endpoint: `createsubscriberid`
   - Description: Create a unique subscriber ID using the subscriber's name.
   
2. **Get Subscriber ID:**
   - Endpoint: `getsubscriberid`
   - Description: Retrieve the unique subscriber ID using the subscriber's name.
   
3. **Subscribe to a Topic:**
   - Endpoint: `subscribe`
   - Description: Subscribe to a specific topic using the topic ID and subscriber ID.
   
4. **Notify Subscribers:**
   - Endpoint: `notify`
   - Description: Notify all subscribers of a specific topic.
   
5. **Unsubscribe from a Topic:**
   - Endpoint: `unsubscribe`
   - Description: Unsubscribe from a specific topic using the topic ID and subscriber ID.

### Handled Edge Cases
1. **Subscriber tries to subscribe to the topic again:** The user will not subscribe twice to the same topic.
2. **Subscriber tries to unsubscribe from the topic even if not subscribed:** Appropriate error handling for this case.
3. **Invalid SubscriberID:** The SubscriberID should be alphanumeric and 6 characters long. Users need to create a SubscriberID first.
4. **Invalid topicID:** Only the following topics are allowed: `Os`, `Oop`, `DBMS`, `Blockchain`. Appropriate errors will be shown for other inputs.
5. **Subscribe to a non-existing topic:** Users cannot subscribe to topics that are not available/created.
6. **Notify with no subscribers:** The notify API handles the case where no subscribers have subscribed to the topic.

### Sample
Here is an example usage of the APIs.
