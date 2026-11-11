import re


class DocumentProcessor:

    def clean_text(self, text):
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text

    def split_text(self, text, chunk_size=500):
        words = text.split()
        chunks = []

        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)

        return chunks

    def process_document(self, text):
        cleaned_text = self.clean_text(text)
        chunks = self.split_text(cleaned_text)
        return chunks