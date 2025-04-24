- [EPICS and User Stories](#epics-and-user-stories)
  - [EPIC 🏰 - Manage Files](#epic----manage-files)
    - [US 🧑‍💻 - View Created Files](#us----view-created-files)
      - [🧪 Aceptance Criteria (Done: ✅ / Pending: ⬜️)](#-aceptance-criteria-done---pending-️)
      - [📝 Tasks (Done: ✅ / Pending: ⬜️)](#-tasks-done---pending-️)
  - [EPIC 🏰 - Create Files](#epic----create-files)
    - [US 🧑‍💻 - Create Files: Create a New Diagram File](#us----create-files-create-a-new-diagram-file)
      - [🧪 Aceptance Criteria (Done: ✅ / Pending: ⬜️)](#-aceptance-criteria-done---pending-️-1)
      - [📝 Tasks (Done: ✅ / Pending: ⬜️)](#-tasks-done---pending-️-1)
    - [US 🧑‍💻 - Create Files: Select the GraphTypes](#us----create-files-select-the-graphtypes)
      - [🧪 Aceptance Criteria (Done: ✅ / Pending: ⬜️)](#-aceptance-criteria-done---pending-️-2)
      - [📝 Tasks (Done: ✅ / Pending: ⬜️)](#-tasks-done---pending-️-2)
    - [US 🧑‍💻 - Create Files: Create Nodes](#us----create-files-create-nodes)
    - [US 🧑‍💻 - Create Files: Edit Nodes](#us----create-files-edit-nodes)
    - [US 🧑‍💻 - Create Files: Create Relationships](#us----create-files-create-relationships)
    - [US 🧑‍💻 - Create Files: Delete Relationships](#us----create-files-delete-relationships)
    - [US 🧑‍💻 - Create Files: Edit Relationships](#us----create-files-edit-relationships)
    - [US 🧑‍💻 - Create Files: Visualize Diagram](#us----create-files-visualize-diagram)
    - [US 🧑‍💻 - Create Files: Save Changes](#us----create-files-save-changes)
  - [EPIC 🏰 - Edit Files](#epic----edit-files)
    - [US 🧑‍💻 - Edit Created Files](#us----edit-created-files)
    - [US 🧑‍💻 - Edit Files: Select Vertical or Horizontal Layout](#us----edit-files-select-vertical-or-horizontal-layout)
    - [US 🧑‍💻 - Edit Files: Create Nodes](#us----edit-files-create-nodes)
    - [US 🧑‍💻 - Edit Files: Edit Nodes](#us----edit-files-edit-nodes)
    - [US 🧑‍💻 - Edit Files: Create Relationships](#us----edit-files-create-relationships)
    - [US 🧑‍💻 - Edit Files: Delete Relationships](#us----edit-files-delete-relationships)
    - [US 🧑‍💻 - Edit Files: Edit Relationships](#us----edit-files-edit-relationships)
    - [US 🧑‍💻 - Edit Files: Visualize Diagram](#us----edit-files-visualize-diagram)
    - [US 🧑‍💻 - Edit Files: Save Changes](#us----edit-files-save-changes)

# EPICS and User Stories
## EPIC 🏰 - Manage Files
### US 🧑‍💻 - View Created Files
**AS** A user **I WANT TO** view previously created diagrams **SO THAT I** can edit them.

#### 🧪 Aceptance Criteria (Done: ✅ / Pending: ⬜️)
1. ⬜️ When the application starts, a list of diagrams names will be displayed.

#### 📝 Tasks (Done: ✅ / Pending: ⬜️)
1. ⬜️ Create all models.
2. ⬜️ Create all controllers.
3. ⬜️ Create View ListDiagrams.

## EPIC 🏰 - Create Files
### US 🧑‍💻 - Create Files: Create a New Diagram File
**AS A** user **I WANT TO** create a new diagram file **SO THAT I** can document processes.

#### 🧪 Aceptance Criteria (Done: ✅ / Pending: ⬜️)
1. ⬜️ When clicking on New, the creation form will open.
2. ⬜️ The form will have the DiagramHeader model atributes as describe in the respective table.
3. ⬜️ By clicking on SAVE, the diagram header will be saved in the database.

#### 📝 Tasks (Done: ✅ / Pending: ⬜️)
1. ⬜️ Create View -> addDiagramHeader

### US 🧑‍💻 - Create Files: Select the GraphTypes
**AS A** user **I WANT TO** select an option of GraphTypes **SO THAT I** can indicate how to read the diagram.

#### 🧪 Aceptance Criteria (Done: ✅ / Pending: ⬜️)
1. ⬜️ In the addDiagramHeader view, add a select list to indicate wich Grap Types corresponds.

#### 📝 Tasks (Done: ✅ / Pending: ⬜️)
1. ⬜️ Create View -> addDiagramHeader
2. ⬜️ By clicking on SAVE, the diagram header will and the asociated Graph Type.

### US 🧑‍💻 - Create Files: Create Nodes
**AS A** user **I WANT TO** create nodes with a code, description, and shape (diamond, rectangle, circle) **SO THAT I** can later associate them in the diagram.

### US 🧑‍💻 - Create Files: Edit Nodes
**AS A** user **I WANT TO** edit all node attributes, except the node code if no relationship has been created for it **SO THAT I** can correct my diagrams.

### US 🧑‍💻 - Create Files: Create Relationships
**AS A** user **I WANT TO** create relationships between nodes **SO THAT I** can build the diagram.

### US 🧑‍💻 - Create Files: Delete Relationships
**AS A** user **I WANT TO** delete relationships **SO THAT I** can remove unnecessary ones.

### US 🧑‍💻 - Create Files: Edit Relationships
**AS A** user **I WANT TO** edit relationships **SO THAT I** can correct any errors.

### US 🧑‍💻 - Create Files: Visualize Diagram
**AS A** user **I WANT TO** visualize how the diagram looks as I create relationships **SO THAT I** can ensure the diagram is assembled correctly.

### US 🧑‍💻 - Create Files: Save Changes
**AS A** user **I WANT TO** automatically save changes **SO THAT** files are persisted and usable in my projects


## EPIC 🏰 - Edit Files
### US 🧑‍💻 - Edit Created Files
**AS A** user **I WANT TO** select a  previously created diagram **SO THAT I** can edit it.

### US 🧑‍💻 - Edit Files: Select Vertical or Horizontal Layout
**AS A** user **I WANT TO** select between horizontal or vertical **TO** indicate whether the diagram is read horizontally or vertically.

### US 🧑‍💻 - Edit Files: Create Nodes
**AS A** user **I WANT TO** create nodes with a code, description, and shape (diamond, rectangle, circle) **SO THAT I** can later associate them in the diagram.

### US 🧑‍💻 - Edit Files: Edit Nodes
**AS A** user **I WANT TO** edit all node attributes, except the node code if no relationship has been created for it **SO THAT I** can correct my diagrams.

### US 🧑‍💻 - Edit Files: Create Relationships
**AS A** user **I WANT TO** create relationships between nodes **SO THAT I** can build the diagram

### US 🧑‍💻 - Edit Files: Delete Relationships
**AS A** user **I WANT TO** delete relationships **SO THAT I** can remove unnecessary ones

### US 🧑‍💻 - Edit Files: Edit Relationships
**AS A** user **I WANT TO** edit relationships **SO THAT I** can correct any errors

### US 🧑‍💻 - Edit Files: Visualize Diagram
**AS A** user **I WANT TO** visualize how the diagram looks as I create relationships **SO THAT I** can ensure the diagram is assembled correctly.

### US 🧑‍💻 - Edit Files: Save Changes
**AS A** user **I WANT TO** save my diagram **SO THAT** files are persisted and usable in my projects.
