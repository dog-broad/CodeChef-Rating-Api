# CodeChef Profile Viewer 🧑‍💻

Welcome to the **CodeChef Profile Viewer**! This Flask-based web application allows users to fetch and view details of CodeChef profiles, including current ratings and other user information.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

## Features ✨

- Enter a CodeChef handle to fetch user details and ratings.
- View the user's current rating, username, country, and whether they have a CodeChef Pro Plan.
- Responsive design with Bootstrap for a seamless user experience.
- Redirects to a detailed profile view upon form submission.

## Installation 🛠️

To set up this project on your local machine, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/CodeChef-Profile-Viewer.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd CodeChef-Profile-Viewer
   ```

3. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

5. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Flask application:**

   ```bash
   python app.py
   ```

   The application will be available at `http://127.0.0.1:8800`.

## Usage 🚀

1. Open your browser and go to `http://127.0.0.1:8800`.
2. Enter a valid CodeChef handle in the input field.
3. Click the "Get Profile" button to view user details.
4. You will be redirected to a page showing the user's current rating and other profile details.

## Credits 🙏

This project is highly inspired by the work of [Deepak Suthar](https://github.com/deepaksuthar40128/Codechef-API). Special thanks to Deepak for providing a foundational reference for this project!

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Hosting 🌐

The application will be hosted on Vercel. You can access it [here](https://your-vercel-deployment-url).

---

Feel free to contribute to this project by submitting issues or pull requests. Happy coding! 😊
