"""This module is a basic language translator"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Return French from English"""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Return English from French"""
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
