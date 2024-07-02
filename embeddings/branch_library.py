import streamlit.components.v1 as st_html

zoom = 0.5

html = f"""
<div style="transform: scale({zoom}); transform-origin: 0 0;">
    <iframe src="https://branchlibrary-8478c72f5159.herokuapp.com/" width="1000" height="1000" scrolling="yes"></iframe>
</div>
"""   

link = st_html.html(html, scrolling=True)


#st_html.iframe(
#    "https://branchlibrary-8478c72f5159.herokuapp.com/", 
#    height=500,
#    scrolling=True
#)
