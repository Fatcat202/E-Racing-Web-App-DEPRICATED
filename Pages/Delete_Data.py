import streamlit as st          #pip install streamlit
import os

#Confirims that the folder either exists or not
folder_exist = os.path.isdir('Trial_Data')
#region popup
#a Confirmation popup to confirms that the user wants to delete the file
@st.dialog("Confirmation popup")
def popup(folder_path, selected_filename):
    st.write(f"ARE YOU SURE YOU WANT TO DELETE {selected_filename} THIS ACTION IS IRREVERSIBLE")
    if st.button("DELETE"):
        result = os.path.join(folder_path, selected_filename)
        # A delete file in the case of accidental deletion or sabotage
        os.makedirs("Deleted_files", exist_ok=True)
        os.replace(f'{result}',f'Deleted_files/{selected_filename}')
        st.rerun()
#endregion popup

# Display title
st.header("Delete Data", divider=True)
# Display sidebar title
st.sidebar.markdown("Delete Data")

#Confirms the Trial data folder exist
with st.sidebar:
    if folder_exist is True:
        st.success("Folder found")
    else:
        st.error("Folder NOT found")

if folder_exist:
    def file_selector(folder_path='Trial_Data'):
        filenames = os.listdir(folder_path)
        #A drop down of all the files that exists in Trial_Data
        selected_filename = st.selectbox('Select a file', ['-- Select a file --'] + filenames)
        if selected_filename == '-- Select a file --':
            return None
        return selected_filename,folder_path
    selection = file_selector()
    if selection is not None:
        filename, folder_path = selection
        st.write(f'You selected `{filename}`')
        #button for file deletion
        if st.button("DELETE FILE"):
            #popup for confirming deletion
            popup(folder_path,filename)
else:
    st.error('Folder not found')