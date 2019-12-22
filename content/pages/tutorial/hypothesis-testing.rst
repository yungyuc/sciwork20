=======================================
Tutorial - Hypothesis Testing in Python
=======================================

:date: 2019-12-18 12:00
:url: tutorial/hypothesis-testing.html
:save_as: tutorial/hypothesis-testing.html

Tutorial - Hypothesis Testing in Python
=======================================

本工作坊將指導學員在 Python 使用統計學之假設檢定，
並使用真實的資料集進行練習，
期待學員能在日常工作中發揮假設檢定之威力。

在實驗中，控制組與實驗組的平均分別是 0.72 與 0.76。
這樣就代表了實驗組比控制組更好嗎？還是差異僅僅來自噪訊呢？
假設檢定就是能夠幫助我們進行判斷的工具，
這場工作坊將帶著學員了解背景知識與進行相應的實作。

(English)

This tutorial will guide attendees to conduct hypothesis testing in Python with
real datasets, and help attendees use it in daily work.

In an experiment, the averages of the control group and the experimental group
are 0.72 and 0.76. Is the experimental group better than the control group? Or
is the difference just due to the noise? Hypothesis testing is the tool to help
us do such judgement.

Goal
====

1. 了解使用假設檢定需要的背景知識。
2. 學會如何在 Python 中實作假設檢定。

(English)

1. Understand the necessary knowledge of using hypothesis testing.
2. Learn how to conduct hypothesis testing in Python.

Target audience
---------------

1. 初學 Python 想了解 Python 更多應用者。
2. Python 工程師想了解 Python 資料科學應用者。
3. 資料科學家想了解 Python 統計學應用者。

(English)

1. People who want to know more applications of Python.
2. People who are Python engineers and want to know more about Python in data
   science.
3. People who are data scientists and want to know more about Python in
   statistics.

Speaker introduction
====================

Mosky Liu／劉依語 (https://mosky.tw)

Mosky 是個熱愛 open source 精神的 Python 工程師，
也是 `Pinkoi <https://pinkoi.com/>`__ 的 Python Charmer，
工作時和同事一起打造能夠買到獨特禮物的設計品購物平台。

自從寫下人生第一支程式後，
就難以忘懷以敘述為磚、邏輯為泥，堆砌出腦中藍圖的成就感，也熱愛分享自己所學。
業餘時是 Python 課程講師，偶爾講點資料科學。
也是數場國內外研討會的講者，包含臺灣的 PyCon、COSCUP、TEDxNTUST，
以及在日本、新加坡、香港、韓國、馬來西亞等地的 PyCon。

(English)

Mosky has love with Python and open source, and is Python Charmer at `Pinkoi
<https://pinkoi.com/>`__, works with colleagues to build the best online
marketplace for unique gifts.

Since writing her first program, she has been using programming language to
script virtual worlds from mental blueprints. She also loves sharing what she
learned. She is teaching Python, working on Python projects, like Clime and
MoSQL, and has spoken at PyCons, COSCUPs, TEDxNTUST in Taiwan, and PyCons in
Japan, Singapore, Hong Kong, Korea, and Malaysia.

Detail description
==================

在這場工作坊，講師會指導如何使用 Python 計算 p-value、power 與 sample size，
同時講解關於 p-value 常見的誤解以及 α、power、β 與 confidence level
之間的關係，最後介紹常見的測試與完整的測試指南。

假設檢定通常用於實驗研究，以判斷治療／修改是否有效。
但在工程中的品質控制也非常好用。例如我們可以監控特定功能使用成功率，
利用假設檢定判斷是否需要介入。講師將在課程中詳細介紹。

(English)

In this tutorial, I will introduce how to calculate the p-value in Python by
examples, the common misunderstandings of p-values, how to calculate the power
and the sample size, the relationships among α, power, confidence level, β, the
common tests, and finally an overall guide to do a hypothesis test,

We usually use hypothesis testing for the experiments in research, but it is
also useful for the quality control in industry, e.g., we can monitor the
success ratio of a specific feature and use hypothesis testing to judge whether
we need to step in. I will expand the details in the tutorial.

Requirement
-----------

1. 本工作坊不包含 Python 基本語法，參加者必須了解 Python 基本語法。
2. 本工作坊會包含機率、統計學與 Python 資料處理與科學計算等內容。
   講師不會詳加介紹，但歡迎學員提問。

(English)

1. Attendees should understand the basic Python syntax.
2. This tutorial will mention probability, statistics, Python data processing
   and scientific computing, but won't introduce them. The attendees are still
   welcome to ask about the details.
