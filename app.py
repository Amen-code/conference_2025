import streamlit as st



def generate_card(name, university):
    st.write(f"**{name}**")
    st.write(f"*{university}*")

def generate_names(name):
    st.write(f"**{name}**")
    
def main():
    st.set_page_config(" Hammamet conference 2024-2025",page_icon="Logo.png")
    st.title("Stochastics in Mathematical Finance and Physics Conference")
    st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)
    st.markdown("Time and place: <i class='fas fa-clock'></i> Oct. 20-Oct. 24, 2025, <i class='fas fa-map-marker-alt'></i> Radisson Blue Resort Thalasso, Hammamet, Tunisia", unsafe_allow_html=True)
    st.write("---")
    st.write("The conference is an occasion to bring together researchers in the beautiful Hammamet to discuss recent developments in stochastics with applications to mathematical physics and finance. The link of the previous conference is available [here](https://www.mn.uio.no/math/english/research/projects/storm/events/conferences/Stochastics%20in%20Mathematical%20Finance%20and%20Physics/).")
    # Display conference name
    
    st.markdown("""
    
    """,unsafe_allow_html=True)
    st.markdown(
        """
       <style>
       footer {visibility:hidden;}
       #MainMenu {visibility: hidden;}
       [data-testid="stSidebar"][aria-expanded="true"]{min-width: 250px;max-width: 250px;}
       </style>
       """,
        unsafe_allow_html=True,
    )  

    # Display hotel image
    
    st.image('hotel.jpg', width = 600 ,output_format = "JPEG")
    st.write("---")

    st.write(" The link of the previous conference is available  [here](https://conference-hammamet.streamlit.app).")
    # Call for Abstract 
    st.subheader(":blue[Call for Abstracts]")
    st.write("A call for abstract is open to propose a contributed talk or a poster. There are limited slots for contributed talks. The form is [here](https://forms.gle/FXaQ37w8x7CHxDL99).")
    st.error("Deadline for submission is September 5th. You will be notified about your proposed talk/poster within September 15th.")
    
    #Program
    
    st.subheader(":blue[Program]")
    st.write("\nA full list of speakers will be available together with the program. This includes:")
    # List of speakers
    plenary_speakers = [
        "Fred Espen Benth", "Tahir Chouli", "Abderrazek Karoui", "Antonis Papapantoleon", "Ivan Nourdin",
        "Sebastian Kassing", "Sonia Mazzucchi", "Michael Kupper"
    ]
    
    invited_speakers = [
        "Nacira Agram", "Griselda Deelstra", "Christa Cuchiero", "Anis Matoussi", "Chiheb Ben Hamouda", 
        "Youssef Ouknine", "Stefania Ugolini", "Luigi Borasi", "Jean Daniel Mukam", "Stefan Tappe",
        "Wissal Sabagh", "Max Sauerbrey", "Barbara Rudiger", "Bernt Oksendal", 
        "Michele Vanmaele" , "Giulia Di Nunno", "Josef Teichmann", "Olfa Draouil","Astrid Hilbert","Martin Friesen","Nizar Touzi","Caroline Hillairet","Asma Khedher"
    ]
    Contributed_speakers = ["Mariem Abdellatif","Kaoutar Nasroallah","Mohammed Amine Jalal","Irene Ventura","Mohamed Louriki","Ihsan Arharas"]
    # Sort the speakers alphabetically by last name
    plenary_speakers_sorted = sorted(plenary_speakers, key=lambda name: name.split()[-1])
    invited_speakers_sorted = sorted(invited_speakers, key=lambda name: name.split()[-1])
    Contributed_speakers_sorted = sorted(Contributed_speakers, key=lambda name: name.split()[-1])
    # Display Plenary Speakers
    st.subheader("List of confirmed Plenary speakers")
    for i in range(0, len(plenary_speakers_sorted), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(plenary_speakers_sorted):
                with col:
                    generate_names(plenary_speakers_sorted[i + j])
    
    st.write("---")
    
    # Display Invited Speakers
    st.subheader(" List of confirmed Invited speakers")
    for i in range(0, len(invited_speakers_sorted), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(invited_speakers_sorted):
                with col:
                    generate_names(invited_speakers_sorted[i + j])
    
    st.write("---")

    # Display Invited Speakers
    st.subheader(" List of confirmed Invited speakers")
    for i in range(0, len(Contributed_speakers_sorted), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(Contributed_speakers_sorted):
                with col:
                    generate_names(Contributed_speakers_sorted[i + j])
    
    st.write("---")

    # Button to register (redirects to Google Form)
    st.subheader(":blue[Registration]")
    st.write("The registration form is available [here](https://docs.google.com/forms/d/e/1FAIpQLScJtPavmI45WvgrrMSHVJUc6xAcEktuBd--JZ53DgQWjVBZXg/viewform).")
    st.write("Arrival and departure form is available [here](https://docs.google.com/forms/d/e/1FAIpQLSdlT_ZsluYUIvS6xoM3ubXn7oDbvxRQudjvBJl6Iv6Yavubnw/viewform?usp=sf_link).")

    st.error("Deadline for Registration is September 5th.")
    # URL for the International airport of Tunis-Carthage
    airport_url = "https://www.tunis-airport.com"

    # Adding a link to the airport within the Transport section
    st.subheader(":blue[Transport]")
    st.markdown("The best way to reach the conference venue for international participants is to fly to the [International airport of Tunis-Carthage]({}). Local transportation between the airport and the conference hotel is organized and included in the rates. Please fill the registration form above to secure the service.".format(airport_url))

    hotel_name = "Radisson Blue Resort Thalasso, Hammamet"
    hotel_url = "https://www.radissonhotels.com/en-us/hotels/radisson-blu-resort-hammamet"

    st.subheader(":blue[Fees]")
    st.markdown(f"The conference is organised at the **[{hotel_name}]({hotel_url})**. The hotel provides all the necessary services for the event in a beautiful location. The local organisers have arranged some special rates for the days of the event for the registered participants: Full-board basis (night, breakfast, lunch, coffee breaks, dinner, transportation from Tunis airport to the hotel, excursion and conference dinner).")
    st.subheader(":blue[Excursion ]")
    st.markdown('We are organizing a guided excursion to the Amphitheatre of El Jem, a remarkable historical site known for its impressive Roman architecture and well-preserved condition. A professional guide will accompany the group to ensure an informative and enriching experience.The excursion will take place on Wednesday, followed by a Conference dinner in the evening. There are no additional fees for the excursion.')
    st.image('EL Jam.jpg', width = 600 ,output_format = "JPEG")

    st.subheader(":blue[Sponsors]")
    st.write("This event is organized by the collaboration of several universities and organizations. Financial support is also received from FWO Scientific Research Network ModSimFIE, DAAD- Deutscher Akademischer Austauschdienst with funds from the German Foreign Office and Swedish Research Council grants (2020-04697)")

    st.subheader(":blue[Organizers]")
    organizers = [
    ("Saloua Mani Aouadi", "Tunis El Manar University"),
    ("Giulia di Nunno", "University of Oslo"),
    ("Olfa Draouil", "Tunis El Manar University"),
    ("Martin Friesen", "Dublin City University"),
    ("Astrid Hilbert", "Linnaeus University"),
    ("Asma Khedher", "University of Amsterdam"),
    ("Bernt Øksendal", "University of Oslo"),
    ("Barbara Rüdiger", "Bergische University Wuppertal"),
    ("Josef Teichmann", "ETH Zürich"),
    ("Nizar Touzi", "New York University"),
    ("Michèle Vanmaele", "Ghent University"),
    
]
    for i in range(0, len(organizers), 3):
        row = organizers[i:i+3]
        col1, col2, col3 = st.columns(3)

        with col1:
            if i < len(organizers):
                generate_card(row[0][0], row[0][1])
        with col2:
            if i + 1 < len(organizers):
                generate_card(row[1][0], row[1][1])
        with col3:
            if i + 2 < len(organizers):
                generate_card(row[2][0], row[2][1])
    st.write("---")
    
if __name__ == '__main__':
    main()
