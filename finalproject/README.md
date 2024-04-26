# Intermediate Written Submission

## Framework and Database

For this web development project, I have chosen to use the Django framework because of its simplicity and integrated support for SQLite, which is suitable for this project's scale. Django's built-in functionalities will facilitate rapid development and easy configuration of the web application.

### NBA Team Model
**Attributes:**
- team_name: String; stores the name of the NBA team.
  - Validation: Length validation to ensure the team name is between 3 and 50 characters.
- founded_year: Integer; stores the year the team was founded.
  - Validation: Numerical validation to ensure the year is within a realistic range for NBA teams (1946 to present).
- championships_won: Integer; stores the number of championships won.
  - Validation: Numerical validation to ensure the number is non-negative.
### NFL Team Model
**Attributes:**
- team_name: String; stores the name of the NFL team.
  - Validation: Length validation to ensure the team name is between 3 and 50 characters.
- head_coach: String; stores the name of the head coach.
  - Validation: Regex validation to ensure the name contains only letters and spaces, and is at least 5 characters long.
- super_bowl_wins: Integer; stores the number of Super Bowl victories.
  - Validation: Numerical validation to ensure the number is non-negative and does not exceed a plausible maximum (e.g., 10).


## Client-Side Feature Implementation

For the NBA teams index page, client-side sorting has been implemented to organize teams by any column heading—such as 'team_name', 'founded_year', or 'championships_won'. This feature enables users to sort the table data in both ascending and descending order by clicking the relevant column header, all without needing to reload the page.
## Logic for Client-Side Sorting

**HTML Elements:**
- Each column header is wrapped in a <th> tag that is made clickable through JavaScript.

**JavaScript Functionality:**
- Click events are bound to each column header.
- When a header is clicked, the function determines the current sort order and toggles it.
- The table data is then sorted based on the selected column in the newly determined order.
- The DOM (Document Object Model) is updated to display the records in this order, offering a dynamic and responsive user experience.

## Challenges and Solutions

**Challenge:**
- Initially, the client-side sorting for 'championships_won' treated numeric values as strings, leading to incorrect sorting behavior.

**Solution:**
- Adjusted the JavaScript sorting function to detect numeric columns and parse the cell values as integers before comparing, ensuring accurate numeric sorting.

**Challenge:**
- I wanted to use Rails, but I decided to try Django since I haven’t had much practice with it. This had me confused on how Django operated versus how Rails operated, which I was much more familiar with it.
  
**Solution:**
- I started looking at notes and stackoverflow to see what directories were necessary where and which files needed to be created to show the view pages.
