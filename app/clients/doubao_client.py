"""
Doubao client for game task generation and story analysis.
This client is currently mocked, but will be connected to real Doubao API later.
"""

class DoubaoClient:
    """Client for Doubao service"""

    def generate_tasks(self, character: dict, image_caption: str) -> list:
        """
        Generate game tasks for the given character and image context.

        Input:
            - character: Main character information
            - image_caption: Description of the initial image

        Output:
            - List of 3 generated tasks
        """
        # Mock implementation
        return [
            {
                "id": "task_1",
                "description": "Find the hidden treasure map",
                "target_state": "Locate the treasure map",
                "difficulty": "easy"
            }
        ] * 3

    def analyze_story(self, story_text: str, tasks: list, task_status: dict) -> dict:
        """
        Analyze story and provide rating.

        Input:
            - story_text: Complete story text
            - tasks: Original game tasks
            - task_status: Completion status of each task

        Output:
            - Analysis result with rating
        """
        # Mock implementation
        return {
            "stars": 3,
            "comment": "Great story! You completed all tasks.",
            "story_type": "Adventure"
        }

# Singleton client instance
doubao_client = DoubaoClient()
