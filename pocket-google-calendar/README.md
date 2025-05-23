# Pocket Google Calendar

An application based on the Pocket Flow framework for Google Calendar integration.

## 📋 Description

This project implements a Google Calendar integration using the Pocket Flow framework, allowing efficient management of events and appointments through a simple and intuitive interface.

## 🚀 Features

- Google Calendar API Integration
- Event Management
- Appointment Viewing
- Flow-based Interface using Pocket Flow

## 🛠️ Technologies Used

- Python
- Pocket Flow Framework
- Google Calendar API
- Pipenv for dependency management

## 📦 Installation

1. Clone the repository:
```bash
git clone [REPOSITORY_URL]
cd pocket-google-calendar
```

2. Install dependencies using Pipenv:
```bash
pipenv install
```

3. Configure Google Calendar credentials:
   - Follow the [Google Calendar API](https://developers.google.com/calendar/api/guides/auth) instructions
   - Place the credentials file in the project directory

## 🔧 Configuration

1. Activate the virtual environment:
```bash
pipenv shell
```

2. Run the application:
```bash
python main.py
```

## 📁 Project Structure

```
pocket-google-calendar/
├── main.py           # Application entry point
├── nodes.py          # Pocket Flow node definitions
├── utils/            # Utilities and helper functions
├── Pipfile           # Pipenv configuration
└── token.pickle      # Google Calendar authentication token
```

## 🤝 Contributing

1. Fork the project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is under the MIT License. See the [LICENSE](LICENSE) file for more details.

## ✨ Acknowledgments

- [Pocket Flow](https://github.com/the-pocket/PocketFlow) - Framework used
- [Google Calendar API](https://developers.google.com/calendar) - Integration API 