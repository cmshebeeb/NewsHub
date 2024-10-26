https://www.notion.so/NewsHUB-12bd150d1b28804a8b8dcfe3d06ab4bb?pvs=4

# NewsHub

| Days | Tasks                                     | Team Responsible         | Tips for Effective Use                                         | How to Do It                                                      | Resources                     |
|------|-------------------------------------------|--------------------------|---------------------------------------------------------------|-------------------------------------------------------------------|-------------------------------|
| 1    | Kickoff Meeting                           | All Teams                | Set clear goals and expectations.                             | Schedule a meeting via Zoom/Google Meet.                         | Zoom                          |
| 2    | Requirements Gathering                    | All Teams                | Use simple language to document features.                     | Discuss features and write them down in Google Docs.             | Google Docs                   |
| 3    | Design UI/UX Mockups                     | Team A                   | Keep designs simple and user-friendly.                        | Use Figma to create wireframes for key pages.                    | Figma                         |
| 4    | Review Designs with Teams                 | All Teams                | Collect feedback and ensure alignment across teams.           | Present mockups in a meeting, gather feedback, and make revisions.| Google Slides                 |
| 5    | Set Up Development Environment            | Teams A, B, C           | Follow guides carefully to avoid mistakes.                    | Install Node.js, React, and MongoDB following online tutorials.  | Node.js, MongoDB              |
| 6    | Set Up Development Environment            | Teams A, B, C           | Organize project files clearly.                               | Use create-react-app for frontend and create a folder structure for backend.| React Setup Guide             |
| 7    | Implement Frontend Registration/Login     | Team A                   | Start with templates for forms.                               | Create a registration form in React using controlled components.  | React Forms                   |
| 8    | Implement Frontend Preferences Selection   | Team A                   | Keep the user interface intuitive.                             | Build a preferences selection component with checkboxes/dropdowns.| React Select                  |
| 9    | Implement Backend User Management         | Team B                   | Focus on one API endpoint at a time.                          | Set up Express server and create routes for registration.         | Express.js                    |
| 10   | Implement Backend User Management         | Team B                   | Test each endpoint as you create it.                          | Use Postman to test registration and login APIs.                 | Postman                       |
| 11   | Fetch News Articles from API              | Team B                   | Read API documentation carefully.                             | Register for NewsAPI, then create a GET endpoint to fetch articles.| NewsAPI                       |
| 12   | Fetch News Articles from API              | Team B                   | Check the data structure returned by the API.                 | Test the fetching process and ensure correct data retrieval.      | Axios Documentation           |
| 13   | Display News Feed on Frontend             | Team A                   | Start with a simple layout for displaying articles.          | Create a NewsFeed component that renders articles from state.     | React State                   |
| 14   | Display News Feed on Frontend             | Team A                   | Add CSS styles for better presentation.                       | Use CSS or a framework like Bootstrap to style the news articles. | Bootstrap                     |
| 15   | Implement Basic ML Features               | Team C                   | Start simple with content-based filtering.                    | Research and build a basic recommendation model using sample data.| Scikit-learn                  |
| 16   | Implement Basic ML Features               | Team C                   | Document your modeling process to track learning.             | Collect and preprocess data, then train your model with scikit-learn.| Kaggle Datasets               |
| 17   | Integrate ML with Backend                 | Team C                   | Ensure data flow is clear between the frontend and ML model. | Create an endpoint that calls the ML model for recommendations.   | Flask or Express Integration   |
| 18   | Integrate ML with Backend                 | Team C                   | Debug any issues that arise during testing.                  | Test the ML endpoint by calling it from the frontend and checking responses.| Debugging Tools              |
| 19   | Conduct Unit Testing                      | All Teams                | Focus on testing individual components first.                 | Each team should write and run unit tests for their features.     | Jest for React                |
| 20   | Conduct Integration Testing                | All Teams                | Test how well all components interact with each other.       | Perform integration tests and document any issues that arise.     | Cypress                       |
| 21   | Gather User Feedback                      | All Teams                | Use clear questions in your survey to gather feedback.       | Create a Google Form to collect feedback on usability and features.| Google Forms                  |
| 22   | User Feedback Collection                  | All Teams                | Analyze feedback for common trends and issues.               | Review survey results together and prioritize improvements.       | Google Sheets                 |
| 23   | Iterate Based on Feedback                 | All Teams                | Assign tasks based on user feedback to make adjustments.     | Create a list of prioritized changes and assign them to team members.| Trello for Task Management    |
| 24   | Prepare for Deployment                    | Teams A, B               | Review all deployment steps and configurations.              | Ensure all environment variables and dependencies are set.        | Heroku Deployment Guide       |
| 25   | Deploy the Application                    | All Teams                | Double-check that everything works in the live environment.  | Deploy the backend to Heroku and frontend to Netlify or Vercel.  | Netlify Deployment Guide      |
| 26   | Final Testing Post-Deployment             | All Teams                | Conduct thorough testing on the live application.            | Test all functionalities, looking for bugs or performance issues. | Monitoring Tools              |
| 27   | Monitor Performance                       | All Teams                | Use analytics tools to observe user engagement and system load.| Set up Google Analytics to track user interaction data.          | Google Analytics              |
| 28   | Gather Ongoing Feedback                   | All Teams                | Continue to collect user feedback for further improvements.   | Send out periodic surveys to users for their thoughts on the app. | SurveyMonkey                  |
| 29   | Plan for Future Enhancements              | All Teams                | Discuss ideas for new features based on user input.         | Hold brainstorming sessions to prioritize features for the next phase.| Miro for Brainstorming       |
| 30   | Document the Project                      | All Teams                | Create thorough documentation for future reference.          | Write a project overview, setup instructions, and API documentation.| Markdown Guide                |


# Day 1: Kickoff Meeting

## Functions/Tasks
- **Team Meeting:** Gather all team members for a kickoff meeting.
- **Define Goals:** Establish clear project goals and objectives.
- **Assign Roles:** Define specific roles and responsibilities for each team.

## Team Responsible
- All Teams (Team A, Team B, Team C)

## Tips for Effective Use
- Create a meeting agenda to ensure all topics are covered.
- Encourage open communication and feedback from all team members.

## How to Do It
1. **Schedule the Meeting:** Use Zoom or Google Meet to set up a virtual meeting.
2. **Prepare the Agenda:** Share the agenda in advance, focusing on project goals, expectations, and role assignments.
3. **Discussion:** Allow time for each team to present their initial thoughts on the project.

## Resources Needed
- Video conferencing tools (e.g., Zoom, Google Meet)
- Google Docs for taking notes during the meeting
- A shared document to track action items




# Day 2: Requirements Gathering
## Functions/Tasks
- **Identify Features:** List the essential features needed for the application (e.g., user login, news feed).
- **Create User Stories:** Develop user stories to define functionality from the user’s perspective.
## Team Responsible
- All Teams (collaboratively)
## Tips for Effective Use
- Use clear and simple language to ensure everyone understands the requirements.
- Document everything clearly for future reference.
## How to Do It
1. **Hold a Collaborative Session:** Use Google Docs for real-time writing and collaboration.
2. **Facilitate Discussion:** Encourage each team to share ideas for features.
3. **Write User Stories:** Develop user stories such as "As a user, I want to view news articles based on my interests."
## Resources Needed
- Google Docs for collaborative writing
- Access to user story templates or examples online


# Day 3: Design UI/UX Mockups
## Functions/Tasks
-**Create Wireframes:** Design the layout for key pages (registration, login, news feed).
-**User Flow:** Map out the navigation process for users within the application.
## Team Responsible
- Team A
## Tips for Effective Use
- Keep the design simple and user-friendly.
- Utilize existing templates as a foundation to save time.
## How to Do It
1. **Open Figma:** Start a new project for UI mockups.
2. **Design the Layout:** Use shapes and text boxes to represent different UI elements (buttons, forms, etc.).
3. **Get Feedback:** Share mockups with other teams and collect their feedback.
## Resources Needed
- Figma (https://www.figma.com/) for design
- Tutorials on using Figma (available on YouTube)


# Day 4: Review Designs with Teams
## Functions/Tasks
-**Present Mockups:** Showcase the designs created in Figma.
-**Gather Feedback:** Collect input from other teams to refine the design.
## Team Responsible
- All Teams
## Tips for Effective Use
- Be open to constructive criticism and suggestions for improvement.
- Keep feedback focused on usability and functionality.
## How to Do It
1. **Schedule a Meeting**: Use video conferencing tools to present the designs.
2. **Show Each Mockup:** Walk through each design, explaining its purpose and functionality.
3. **Collect Feedback:** Record comments and suggestions in a shared document for future reference.
## Resources Needed
- Video conferencing tools (e.g., Zoom, Google Meet)
- Figma for sharing designs
- Google Docs for documenting feedback
