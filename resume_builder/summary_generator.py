from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()




class SummaryGenerator:
    def __init__(self):
        # Using a model supported by the free tier
        self.model = 'meta-llama/Llama-3.2-1B-Instruct'
        self.api_key = os.getenv('HF_API_KEY')
       
        self.client = InferenceClient(
            model=self.model,
            api_key=self.api_key,
        )
        
        
    def generate_summary(self, occupation, skills):
        '''
        Generates a concise summary for a resume based on the provided skills, languages, and educations.
        Args:
            occupation: A string.
            skills (list): A list of ResumeSkills objects.
        Returns:
            str: The generated summary.
        '''
        

        skills_lst = [f"{skill.skill_name} ({skill.skill_level})" for skill in skills]
        
        skills_str = ', '.join(skills_lst) if skills_lst else 'Not specified'
        
        messages = [
            {
                "role": "user",
                "content": f"Generate a concise professional summary (3-4 sentences) for a {occupation} resume based on:\n\nSkills: {skills_str}\n\nHighlight strengths and qualifications."
            }
        ]
        
        response = self.client.chat_completion(
            model=self.model,
            messages=messages,
            max_tokens=150,
            temperature=0.7,
        )
        
        summary = response.choices[0].message.content.strip()
        
        # Clean up unwanted prefixes
        unwanted_prefixes = [
            "Here's a concise professional summary for your resume:",
            "Here's a professional summary:",
            "Here's a summary:",
            "Professional Summary:",
            "Summary:",
            "Here is a concise professional summary for a resume based on the provided skills:",
            "Here's a concise professional summary for a resume:",
            "Here's a concise professional summary based on your skills:",
        ]
        
        for prefix in unwanted_prefixes:
            if summary.lower().startswith(prefix.lower()):
                summary = summary[len(prefix):].strip()
        
        return summary
