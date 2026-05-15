# OrderNa

OrderNa is a lightweight digital menu, table booking, and WhatsApp-ordering system tailored for local Kenyan restaurants, hotels, and cafes. It is designed to run efficiently on minimal infrastructure, removing the barrier of expensive or specialized point-of-sale hardware.

This repository serves as an isolated module within a multi-app ecosystem managed under the centralized Django marketplace, **BizApp Central**.

---

## Core Features

* **Digital Menu Browser:** A fast, responsive, and mobile-first menu display for customers.
* **Local Table Booking Tracking:** Simple scheduling and management engine for table reservations.
* **WhatsApp Checkout Action:** Instantly formats cart details and dispatches orders directly to a vendor's phone number as a structured chat message.

---

## Architectural Blueprint & Constraints

* **Framework:** Django (Python 3.14+)
* **Database:** SQLite (Phase 1 local testing and lightweight staging)
* **Frontend:** Tailwind CSS via CDN for streamlined UI layouts
* **Media Storage:** Cloudinary integration
* **Dependency Constraint:** The Python `Pillow` library is bypassed to eliminate compilation conflicts under Python 3.14. Database models handle images using `FileField` instead of `ImageField`.

---

## Project Structure

```text
OrderNa/
├── config/              # Central project configuration and routing
├── menu/                # Application module for menus, items, and bookings
│   ├── migrations/      # Database schema state files
│   ├── admin.py         # Admin dashboard configuration
│   ├── models.py        # Database definitions (Category, MenuItem, TableBooking)
│   └── views.py         # Interface controllers and checkout utilities
├── templates/           # Global layout architecture
├── manage.py            # Django project management script
└── requirements.txt     # Python dependency manifest
