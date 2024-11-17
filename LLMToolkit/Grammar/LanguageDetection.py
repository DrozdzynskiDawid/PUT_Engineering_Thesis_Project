from lingua import Language, LanguageDetectorBuilder
from ..ModuleException import *

def getLanguageConfidenceValue(text: str, top: int):
    if type(text) != str or type(top) != int:
        getTypeError()
    all_languages = Language.all()
    detector = LanguageDetectorBuilder.from_languages(*all_languages).build()
    confidence_values = detector.compute_language_confidence_values(text)
    sorted_confidence_values = sorted(confidence_values, key=lambda c: c.value, reverse=True)
    # get only top languages and compute values again
    top_languages = [confidence.language for confidence in sorted_confidence_values[:top]]
    top_detector = LanguageDetectorBuilder.from_languages(*top_languages).build()
    top_confidence_values = top_detector.compute_language_confidence_values(text)
    result = [
        {"language": confidence.language.name, "confidence": confidence.value}
        for confidence in top_confidence_values
    ]
    return result
