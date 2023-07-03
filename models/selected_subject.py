#!/usr/bin/python3

"""
Handles user's selected subject
"""

from models.base_model import BaseModel, db
from models.user import User
from models.subject import Subject

class SelectedSubject(BaseModel):
    """
    Selected subject class
    """
    __tablename__ = 'selected_subject'
    user_id = db.Column(db.String(126), db.ForeignKey('users.id'), nullable=False)
    subject_id = db.Column(db.String(126), db.ForeignKey('subjects.id'), nullable=False)
    is_compulsory = db.Column(db.Boolean, default=False)

    @classmethod
    def get_complusory_sub(cls, user_id):
        """
        Makes a subject complusory
        """
