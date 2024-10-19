# Contributing to GSheetDB

Thank you for considering contributing to **GSheetDB**! 🎉 Your contributions help make this project better for everyone. Below are guidelines to help you get started.

## Table of Contents

1. Getting Started  
2. Project Setup  
3. How to Contribute  
4. Code of Conduct  
5. Submitting Issues  
6. Submitting Pull Requests  
7. Testing  
8. License

---

## Getting Started

1. **Fork the Repository**:  
   Start by forking the repository to your own GitHub account.

2. **Clone Your Fork Locally**:  
   Use the following command to clone your fork:

   git clone https://github.com/nahom-d54/GSheetDB.git  
   cd GSheetDB

3. **Create a Branch for Your Contribution**:  
   Use a descriptive branch name related to the feature or issue you are addressing:

   git checkout -b feature/improve-query-support

---

## Project Setup

1. **Install Dependencies**:  
   Install the required Python packages using:

   pip install -r requirements.txt

2. **Set Up Service Account**:  
   - Create a **service account** in Google Cloud.  
   - Share your Google Sheets with the **service account email**.  
   - Place the **service account JSON** in the root of your project as service_account.json.

3. **Run Tests to Ensure Everything Works**:

   python -m unittest discover tests/

---

## How to Contribute

1. **Pick an Issue**:  
   Browse the Issues tab and choose one to work on. If you don’t see an issue matching your interests, feel free to create a new one.

2. **Make Changes**:  
   Implement your feature or bug fix and ensure everything works.

3. **Commit Your Changes**:  
   Write clear and concise commit messages:

   git add .  
   git commit -m "Add feature to improve query support"

4. **Push Your Branch**:

   git push origin feature/improve-query-support

5. **Open a Pull Request**:  
   Go to the original repository on GitHub and open a pull request from your branch.

---

## Code of Conduct

Please follow the project’s Code of Conduct when interacting with others.

---

## Submitting Issues

If you find a bug or have a feature request, please open an issue in the Issues tab with a clear description.

---

## Submitting Pull Requests

When submitting a pull request:

1. Ensure your changes are well-tested.
2. Provide a clear description of what you’ve implemented or fixed.
3. Reference any related issues in the description.

---

## Testing

Run the test suite to ensure everything works:

python -m unittest discover tests/

---

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
