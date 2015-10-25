#coding:utf-8

from python_simsimi import SimSimi
from python_simsimi.language_codes import LC_CHINESE_SIMPLIFIED
from python_simsimi.simsimi import SimSimiException
import sys

reload(sys)  
sys.setdefaultencoding('utf8')
simSimi = SimSimi(
        conversation_language = LC_CHINESE_SIMPLIFIED,
        conversation_key = 'YOUR KEY'
)

def chat(input):
	return simSimi.getConversation(input)['response']