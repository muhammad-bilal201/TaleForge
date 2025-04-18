# 📖 TaleForge: A Collaborative Storytelling Platform

TaleForge is a Django-based web platform where creative writers can collaboratively build **branching, choose-your-own-adventure** style stories. Inspired by Reddit and creative writing forums, TaleForge allows users to write, contribute, vote, and explore dynamic storylines together.

---

## 🎯 Project Objective

Build a full-stack Django application where:

- Users can register and manage profiles with avatars and bios.
- Anyone can start a new story and write the first chapter.
- Other users propose new chapters as branches of existing ones.
- Proposed chapters go through a voting system before being added to the story tree.
- Readers can explore stories as branching paths.

---

## 🧱 Core Features

### 1. User Authentication & Profiles
- User Registration, Login, Logout
- Profile with bio and avatar image
- Moderator role (optional for content management)

### 2. Story & Chapter System
- Users can create stories with:
  - Title, genre, and summary
  - Cover image upload
- Each story begins with one chapter
- Chapters follow a tree structure using `django-mptt` for branching
- Only the story creator can mark the story as **completed**

### 3. Chapter Voting & Approval
- New chapters are **pending** until reviewed
- Community members vote to **approve** or **reject**
- Once approved, the chapter becomes an official branch in the story tree
- Voting is limited to **one vote per user per chapter**

### 4. Search & Filters
- Search by story **title** or **genre**
- Filter stories by:
  - Most Voted
  - Recently Updated

### 5. Media Upload
- Avatars for user profiles
- Cover images for stories

---

## 🌟 Bonus Features (Optional)
- 🧭 **Visual Branching Story Map** — View the story structure graphically
- 🔔 **Real-time Notifications** — Get notified when someone adds a chapter to your story
- 📊 **User Dashboard** — Track your writing and voting stats
- 🗳 **Voting Restriction** — Users can only vote once per chapter

---

## 🛠 Tech Stack & Tools

- **Backend:** Django, PostgreSQL (or SQLite for dev)
- **Frontend:** HTML, Tailwind CSS or Bootstrap
- **Tree Structures:** `django-mptt`
- **Forms:** `django-crispy-forms` (optional)
- **Media:** Django file/image handling for avatars & covers

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/taleforge.git
cd taleforge
