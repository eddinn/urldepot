<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>UrlDepot</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.url-modal>Add Url</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(url, index) in urls" :key="index">
              <td>{{ url.title }}</td>
              <td>{{ url.author }}</td>
              <td>
                <span v-if="url.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.url-update-modal
                          @click="editUrl(url)">
                      Update
                  </button>
                  <button
                          type="button"
                          class="btn btn-danger btn-sm"
                          @click="onDeleteUrl(url)">
                      Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addUrlModal"
            id="url-modal"
            title="Add a new url"
            hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addUrlForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addUrlForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addUrlForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editUrlModal"
            id="url-update-modal"
            title="Update"
            hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
            <b-form-input id="form-author-edit-input"
                          type="text"
                          v-model="editForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      urls: [],
      addUrlForm: {
        title: '',
        author: '',
        read: [],
      },
      message: '',
      showMessage: false,
      editForm: {
        id: '',
        title: '',
        author: '',
        read: [],
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getUrls() {
      const path = 'http://localhost:5000/urls';
      axios.get(path)
        .then((res) => {
          this.urls = res.data.urls;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addUrl(payload) {
      const path = 'http://localhost:5000/urls';
      axios.post(path, payload)
        .then(() => {
          this.getUrls();
          this.message = 'Url added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getUrls();
        });
    },
    initForm() {
      this.addUrlForm.title = '';
      this.addUrlForm.author = '';
      this.addUrlForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addUrlModal.hide();
      let read = false;
      if (this.addUrlForm.read[0]) read = true;
      const payload = {
        title: this.addUrlForm.title,
        author: this.addUrlForm.author,
        read, // property shorthand
      };
      this.addUrl(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addUrlModal.hide();
      this.initForm();
    },
    editUrl(url) {
      this.editForm = url;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUrlModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        read,
      };
      this.updateUrl(payload, this.editForm.id);
    },
    updateUrl(payload, urlID) {
      const path = `http://localhost:5000/urls/${urlID}`;
      axios.put(path, payload)
        .then(() => {
          this.getUrls();
          this.message = 'Url updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUrls();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUrlModal.hide();
      this.initForm();
      this.getUrls(); // why?
    },
    removeUrl(urlID) {
      const path = `http://localhost:5000/urls/${urlID}`;
      axios.delete(path)
        .then(() => {
          this.getUrls();
          this.message = 'Url removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUrls();
        });
    },
    onDeleteUrl(url) {
      this.removeUrl(url.id);
    },
  },
  created() {
    this.getUrls();
  },
};
</script>
