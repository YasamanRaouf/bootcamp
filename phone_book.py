import json
import re

FILE_NAME = 'contacts.json'


def load_contacts():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("نام: ")
    phone = input("شماره تلفن: ")
    email = input("ایمیل: ")

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("ایمیل نامعتبر است.")
        return

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("مخاطب جدید اضافه شد.")


def edit_contact(contacts):
    name = input("نام مخاطب برای ویرایش: ")
    for contact in contacts:
        if contact["name"] == name:
            contact["phone"] = input("شماره تلفن جدید: ")
            contact["email"] = input("ایمیل جدید: ")
            save_contacts(contacts)
            print("اطلاعات مخاطب بروزرسانی شد.")
            return
    print("مخاطب یافت نشد.")


def delete_contact(contacts):
    name = input("نام مخاطب برای حذف: ")
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("مخاطب حذف شد.")
            return
    print("مخاطب یافت نشد.")


def display_contacts(contacts):
    for contact in contacts:
        print(f"نام: {contact['name']}, شماره تلفن: {contact['phone']}, ایمیل: {contact['email']}")


def sort_contacts(contacts):
    contacts.sort(key=lambda x: x["name"])
    save_contacts(contacts)
    print("مخاطبین مرتب شدند.")


def main():
    contacts = load_contacts()
    while True:
        print("\nدفترچه تلفن:")
        print("1. اضافه کردن مخاطب جدید")
        print("2. ویرایش مخاطب")
        print("3. حذف مخاطب")
        print("4. نمایش تمام مخاطبین")
        print("5. مرتب سازی مخاطبین")
        print("6. خروج")
        choice = input("انتخاب کنید: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            display_contacts(contacts)
        elif choice == '5':
            sort_contacts(contacts)
        elif choice == '6':
            break
        else:
            print("انتخاب نامعتبر است.")


if __name__ == "__main__":
    main()
