# CodeChef Profile Viewer 🧑‍💻

Welcome to the **CodeChef Profile Viewer**! This Flask-based web application lets users fetch and view CodeChef profiles, including ratings and other details.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)
- [Hosting](#hosting)

## Features ✨

- Enter a CodeChef handle to fetch user details and ratings.
- View the user's rating, username, country, and CodeChef Pro Plan status.
- Responsive design with Bootstrap.
- Redirects to a detailed profile view upon form submission.

## Installation 🛠️

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
3. Click "Get Profile" to view user details.
4. You'll be redirected to a page showing the user's rating and profile details.

## Credits 🙏

Inspired by [Deepak Suthar](https://github.com/deepaksuthar40128/Codechef-API). Thanks for the foundational reference!

## License 📜

MIT License. See the [LICENSE](LICENSE) file for details.

## Hosting 🌐

The application is hosted on [Vercel](https://code-chef-rating-api.vercel.app/).

---

Feel free to contribute by submitting issues or pull requests. Happy coding! 😊

