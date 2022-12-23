import wp_func

first_paragraph_text = "ACCA accountants are diverse finance professionals who approach problems with innovative thinking. What connects them is a qualification that stands for global excellence and the insights, research and continual development throughout their careers from the world’s most forward-thinking accountancy body."

heading_one_text = "Why do we use it"

second_paragraph= "It is a long-established fact that a reader will be distracted by the readable content "
article = wp_func.wp_p(first_paragraph_text) + wp_func.wp_h2(heading_one_text) +wp_func.wp_p(second_paragraph)
print(article)