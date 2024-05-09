import streamlit as st 


############################
#     Paths and Links      #
############################
sidebar_icon = './images/sidebar.png'
github_icon = './images/github.png'
linkedin_icon = './images/linkedin.png'
etl_icon = './images/etl.png'
version_control_icon = './images/version_ctrl.png'
darkOura_icon = './images/DarkOura.png'

app_development = 'https://branchlibrary-8478c72f5159.herokuapp.com/'
linkedin_link = 'https://www.linkedin.com/in/keegan-patton-739362236/'
github_link = 'https://github.com/dbo-keeganpatton'

branch_library_github_link = 'https://github.com/dbo-keeganpatton/fantasci'
branch_library_link = 'https://branchlibrary-8478c72f5159.herokuapp.com/'
dark_oura_github_link = 'https://github.com/dbo-keeganpatton/ourapi'
dark_oura_link = 'https://oura-api-client.streamlit.app/'
retail_pipeline_github_link = 'https://github.com/dbo-keeganpatton/retail_data_pipeline'


############################
#        Main App          #
############################

def main():
    
    st.set_page_config(layout='wide')

    #############################
    #        Side Bar           #
    #############################
 
    with st.sidebar:
        
        st.image(sidebar_icon)

        st.divider()
        st.header(":violet[**Skills**]")
       
        st.code(
            """
            SQL
            Linux
            Python
            PowerBI
            Tableau
            PowerAutomate
            Excel | Google Sheets
            """,
            language='python',
            line_numbers=True
        )
        
        st.divider()
        st.header(":violet[**History**]")
        
        st.code(
            """
            Walmart
            Senior Data Analyst
            # October 2023  ->  Present
            """,
            language='python'
        )

        st.code(
            """
            PAM Transport
            Systems Analyst
            # January 2023 -> October 2023,
            """,
            language='python'
        )
        
        st.code(
            """
            PAM Transport
            Associate Systems Analyst
            # July 2022 -> January 2023
            """,
            language='python'
        )

        
        
    st.title('_Keegan Patton_' )
    
    col1, col2 = st.columns(2,gap="large")
    
    
    #############################
    #           Bio             #
    #############################
    
    with col1:

    
        st.divider()


        sub_col1, sub_col2 = st.columns(2)
        
        with sub_col1:
            st.image("./images/me.png")

        with sub_col2:
            st.header("_Who I am_")
            st.write(
                """
                :family: Father\n
                :skateboard: Skateboarder\n
                :male-technologist: Data Analyst and Programmer\n 
                
                Growth focused, driven and thankful for every day!
                """
            )

        st.divider()

        st.header("_What I do_")
        st.write(
            """
            I am a Senior Data Analyst working for the largest retailer in the world, **:blue[Walmart]** :high_brightness:\n
            In this role I utilize my knowledge of Data Structures, ETL pipelines, Process Automation,
            Business Intelligence and Data Visualization to help drive value for our customers and enable them to\n 
            **:blue[Save Money and Live Better]** :house_with_garden:
            """
        )
    
        
    #############################
    #        Portfolio          #
    #############################

    with col2:
       
        st.divider()
        st.header(':grey[Side Projects]')
       
        # Project1
        with st.expander(
            """**:violet[Automated Data Scraping and Storage Pipeline]** 
            \n*:grey[End2End Data Pipeline]*
            """):
            st.write(
                """
                Comprehensive data pipeline leveraging BeautifulSoup for web scraping, Selenium for web automation, and AWS RDS/EC2 for robust data warehousing and automation.
                """
            )

            st.code(
                """
                AWS Cloud Platform
                Web Automation
                HTML Parsing
                Linux
                """,
                language='sql',
                line_numbers=True
            )
            
            st.page_link(retail_pipeline_github_link, label="Git Repo", icon='🔗')
            st.image(etl_icon)

        # Project2
        with st.expander(
                """**:violet[Branch Library]**
                \n*:grey[Application Development | Backend Dev]*
                """):
            st.write(
                """
                Web application developed in Flask and deployed through Heroku.
                """
            )
            
            st.code(
                """
                Personal Authentication
                Systems Integration
                Backend Development
                ORM Management
                UX Design
                """,
                language='sql',
                line_numbers=True
            )
            
            st.page_link(branch_library_link, label="Deployed App", icon='🔗')
            st.page_link(branch_library_github_link, label="Git Repo", icon='🔗')
            st.write('\n') 
            st.write("*User Version Control System for Application*")
            st.image(version_control_icon) 
        
        
        # Project3
        with st.expander(
            """**:violet[Dark Oura]**
            \n *:grey[Automated Self Service Analytics]*
            """):
            st.write(
                """
                Streamlit Application for Extracting Data from the Oura Ring API.
                """
            )

            st.code(
                """
                Process Automation
                ETL Processing
                Visualization
                """,
                language='sql',
                line_numbers=True
            )
            
            st.page_link(dark_oura_link, label="Live App hosted by Streamlit", icon='🔗')
            st.page_link(dark_oura_github_link, label="Git Repo", icon='🔗')
            st.image(darkOura_icon)
                
        st.write("\n")
        st.write("\n")
        st.write("\n")

        #############################
        #          Links            #
        #############################
   
        subcol3, subcol4 = st.columns([1,7], gap='small')
        with subcol3:
            st.image(github_icon)
        with subcol4:
            st.link_button("GitHub", github_link)
        
        st.write("\n")
        st.write("\n")

        subcol5, subcol6 = st.columns([1,7], gap='small')
        with subcol5:
            st.image(linkedin_icon)
        with subcol6:
            st.link_button("LinkedIn", linkedin_link)
        


if __name__ == "__main__":
    main()
