from difflib import SequenceMatcher
# from sklearn.metrics.pairwise import cosine_similarity

print(SequenceMatcher(None, '다음 화면', '다음 화면 보여').ratio())
