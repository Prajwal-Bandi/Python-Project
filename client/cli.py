"""
    Using cli as client to apply CRUD and store in DB
"""
import requests
import argparse

API_URL = "http://127.0.0.1:5000"

def create_patient(name, age, disease):
    response = requests.post(f"{API_URL}/patients", json={"name": name, "age": age, "disease": disease})
    print(response.json())

def get_patient(patient_id):
    response = requests.get(f"{API_URL}/patients/{patient_id}")
    print(response.json())

def update_patient(patient_id, name, age, disease):
    response = requests.put(f"{API_URL}/patients/{patient_id}",
                            json={"name": name, "age": age, "disease": disease})
    print(response.json())


def delete_patient(patient_id):
    response = requests.delete(f"{API_URL}/patients/{patient_id}")
    print(response.json())

def main():
    parser = argparse.ArgumentParser(description="HMS CLI")
    subparsers = parser.add_subparsers(dest='command')

    create_parser = subparsers.add_parser('create')
    create_parser.add_argument('name')
    create_parser.add_argument('age', type=int)
    create_parser.add_argument('disease')

    get_parser = subparsers.add_parser('get')
    get_parser.add_argument('id', type=int)

    put_parser = subparsers.add_parser('put')
    put_parser.add_argument('id', type=int)
    put_parser.add_argument('name')
    put_parser.add_argument('age', type=int)
    put_parser.add_argument('disease')

    del_parser = subparsers.add_parser('delete')
    del_parser.add_argument('id', type=int)

    args = parser.parse_args()

    if args.command == 'create':
        create_patient(args.name, args.age, args.disease)
    elif args.command == 'get':
        get_patient(args.id)
    elif args.command == 'put':
        update_patient(args.id, args.name, args.age, args.disease)
    elif args.command == 'delete':
        delete_patient(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
