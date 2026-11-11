import os


class DocumentLoader:

    def load_documents(self, folder_path):

        documents = []

        for root, dirs, files in os.walk(folder_path):

            for filename in files:

                if filename.endswith(".txt"):

                    file_path = os.path.join(root, filename)

                    with open(file_path, "r", encoding="utf-8") as file:

                        text = file.read()

                    category = os.path.basename(root)

                    documents.append({
                        "text": text,
                        "category": category,
                        "filename": filename
                    })

        return documents