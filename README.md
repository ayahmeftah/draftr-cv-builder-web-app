# Draftr CV Builder Website

## Introducation
This is the **Draftr CV Builder Web Application**, a platform that allows users to create, manage, and export professional resumes seamlessly.
It was built as part of a project using **Django** and **PostgreSQL**, with cloud storage for handling media files.

Users can choose from different CV templates, manage multiple resumes, and customize sections such as education, experience, and skills.

Below are some screenshots of the application:

<img width="1898" height="905" alt="Image" src="https://github.com/user-attachments/assets/c0ad886f-fead-4a3d-bc69-f940995940bd" />

<img width="1897" height="898" alt="Image" src="https://github.com/user-attachments/assets/02a6568a-c423-47f9-b4a8-714b442a162b" />

<img width="1896" height="906" alt="Image" src="https://github.com/user-attachments/assets/623764fc-a15e-486b-9e74-592a1a1efe0f" />

## Entity-Relationship Diagram (ERD)

<img width="1619" height="880" alt="Draftr ERD" src="https://github.com/user-attachments/assets/f01fec1b-7ea1-4c1f-993f-b6f1d398b084" />


## Features

- **User Authentication** (Sign Up / Login)

- **Create and Manage Multiple CVs** under one account

- **Choose from Professional Templates** for resumes

- **Section Management** – add/remove/edit Education, Experience, Certifications, Projects, Skills

- **File Uploads** (images) stored securely on Cloudinary

- **Download CVs to PDF** for easy sharing and printing

- **Progress Tracker** to guide users through CV creation

## URL Paths  

### General  

| Path                                | Description                     |
|-------------------------------------|---------------------------------|
| `/`                                 | Home page                        |
| `/auth/signup/`                      | User signup page                 |
| `/resumes/templates/`                | List all resume templates        |
| `/resumes/templates/<template_id>/` | Select a template                |
| `/resumes/<resume_id>/personal/`    | Personal info step / Edit        |
| `/resumes/<resume_id>/preview/`     | Preview resume                   |
| `/resumes/<resume_id>/delete/`      | Delete resume                    |
| `/resume/<resume_id>/loader/`       | Resume loader                    |
| `/my-resumes/`                       | List all resumes for current user|

---

### Education  

| Path                                                | Description                     |
|-----------------------------------------------------|---------------------------------|
| `/resumes/<resume_id>/educations/`                 | List education entries           |
| `/resumes/<resume_id>/educations/add/`             | Add education entry              |
| `/resumes/<resume_id>/educations/<education_id>/edit/` | Edit education entry       |
| `/resumes/<resume_id>/educations/<education_id>/delete/` | Delete education entry     |

---

### Experience  

| Path                                                | Description                     |
|-----------------------------------------------------|---------------------------------|
| `/resumes/<resume_id>/experiences/`                | List experience entries          |
| `/resumes/<resume_id>/experiences/add/`            | Add experience entry             |
| `/resumes/<resume_id>/experiences/<experience_id>/edit/` | Edit experience entry       |
| `/resumes/<resume_id>/experiences/<experience_id>/delete/` | Delete experience entry     |

---

### Skills & Skill Categories  

| Path                                                | Description                     |
|-----------------------------------------------------|---------------------------------|
| `/resumes/<resume_id>/skills/`                     | List all skills                  |
| `/resumes/<resume_id>/skill-categories/add/`       | Add skill category               |
| `/resumes/<resume_id>/skill-categories/<category_id>/edit/` | Edit skill category      |
| `/resumes/<resume_id>/skill-categories/<category_id>/delete/` | Delete skill category    |
| `/resumes/<resume_id>/skill-categories/<category_id>/add-skill/` | Add skill to category     |
| `/resumes/<resume_id>/skills/<skill_id>/edit/`    | Edit skill                       |
| `/resumes/<resume_id>/skills/<skill_id>/delete/`  | Delete skill                     |

---

### Projects  

| Path                                                | Description                     |
|-----------------------------------------------------|---------------------------------|
| `/resumes/<resume_id>/projects/`                   | List projects                    |
| `/resumes/<resume_id>/projects/add/`               | Add project                      |
| `/resumes/<resume_id>/projects/<project_id>/edit/` | Edit project                     |
| `/resumes/<resume_id>/projects/<project_id>/delete/` | Delete project                  |

---

### Certifications  

| Path                                                | Description                     |
|-----------------------------------------------------|---------------------------------|
| `/resumes/<resume_id>/certifications/`             | List certifications              |
| `/resumes/<resume_id>/certifications/add/`         | Add certification                |
| `/resumes/<resume_id>/certifications/<certification_id>/edit/` | Edit certification       |
| `/resumes/<resume_id>/certifications/<certification_id>/delete/` | Delete certification   |


## Getting Started

### Prerequisites

- Python 3 installed

- PostgreSQL installed and running

- Virtual environment

- MSYS2 (required for WeasyPrint on Windows, install from [msys2.org](https://www.msys2.org/))

### Installation

1. Clone the repository

```bash
git clone https://github.com/ayahmeftah/draftr-cv-builder-web-app.git  
```

2. Navigate into the project folder

```bash
cd draftr-cv-builder-web-app  
```

3. Create and activate a virtual environment
```bash
python -m venv name-of-venv
source name-of-venv/bin/activate # Mac/Linux
source name-of-venv/Scripts/activate # Windows
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Create a .env file in the root directory and add the following variables:
```env
DB_NAME=your_database_name
DB_PASS=your_database_password

CLOUD_NAME=your_cloudinary_name
API_KEY=your_cloudinary_api_key
API_SECRET=your_cloudinary_api_secret
```

6. Create the PostgreSQL database manually in your local PostgreSQL instance before running migrations.

7. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

8. Create a superuser for admin access
```bash
python manage.py createsuperuser
```

9. Run the development server
```bash
python manage.py runserver
```


## Attributions

- [Cloudinary Setup](https://cloudinary.com/blog/managing-media-files-in-django)

- [Django Docs](https://docs.djangoproject.com/en/5.2/)

- [WeasyPrint](https://pypi.org/project/weasyprint/)

- [CV templates](https://devsnap.me/html-resume-templates)

- [Loader for the CV Build](https://uiverse.io/Nawsome/curly-goose-54)

- [CodePen step progress demos](https://codepen.io/search/pens?q=step+progress+bar)

- [CSS counter for the progress line](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_counter_styles/Using_CSS_counters)

- [Building a progress step ui component using just flex and css](https://stackoverflow.com/questions/51119726/building-a-progress-step-ui-component-using-just-flex-and-css-help-w-labeling)

- [Multistep form with active steps and lines](https://stackoverflow.com/questions/46465744/multistep-form-with-active-steps-and-lines)

- [Google fonts - Poppins](https://fonts.google.com/specimen/Poppins)

- [Brandmark Logo Generator](https://app.brandmark.io/v3/)


## Technologies Used

- Django 

- PostgreSQL

- Python 

- WeasyPrint

- HTML

- CSS

- JavaScript

- Cloudinary 


## Future Enhancements

- Additional CV templates for more customization

- AI-powered CV suggestions and skill matching

- Upload CV and prefill fields

- Export options (Word, JSON)


