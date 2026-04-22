<h1>GreedySearch</h1>

<h2>Description</h2>

<p>Setup and add GreedySearch node into the model during the definition graph step. Type : polymorphic.</p>
<p align="center"><img src="assets/greedysearch.png" alt="GreedySearch" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Graphs in" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>Graphs in : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="input_ids" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>input_ids : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="max_length" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>max_length : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="min_length" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>min_length : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="repetition_penalty" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>repetition_penalty : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="vocab_mask" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>vocab_mask : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="prefix_vocal_mask" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>prefix_vocal_mask : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="attention_mask" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>attention_mask : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="Graphs in" src="assets/Graphs in.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Parameters" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>Parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="decoder" src="assets/cModellvclass.png" width="42"/></td>
      <td valign="top"><strong>decoder : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="decoder_start_token_id" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="42"/></td>
      <td valign="top"><strong>decoder_start_token_id : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="encoder" src="assets/cModellvclass.png" width="42"/></td>
      <td valign="top"><strong>encoder : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="eos_token_id" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="42"/></td>
      <td valign="top"><strong>eos_token_id : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="init_decoder" src="assets/cModellvclass.png" width="42"/></td>
      <td valign="top"><strong>init_decoder : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="model_type" src="/_assets/shared-images/7f/7f7e66ba54dc-cenum.png" width="42"/></td>
      <td valign="top"><strong>model_type : <em>enum</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="no_repeat_ngram_size" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="42"/></td>
      <td valign="top"><strong>no_repeat_ngram_size : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="pad_token_id" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="42"/></td>
      <td valign="top"><strong>pad_token_id : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="vocab_size" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="42"/></td>
      <td valign="top"><strong>vocab_size : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="training?" src="/_assets/shared-images/06/06612771a6c0-cbool.png" width="42"/></td>
      <td valign="top"><strong>training? : <em>boolean</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="lda coeff" src="/_assets/shared-images/c7/c71945e6f909-cdbl.png" width="42"/></td>
      <td valign="top"><strong>lda coeff : <em>float</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="Parameters" src="assets/Parameters.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="name" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="specified_outputs_name" src="/_assets/shared-images/ce/ceeb813734df-c1dstr.png" width="42"/></td>
      <td valign="top"><strong>specified_outputs_name : <em>array of string</em></strong>
<ul>
  <li><img alt="String" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="32"/> <strong>String : <em>string</em></strong></li>
</ul></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="sequences" src="/_assets/shared-images/1f/1f730a978528-ionnxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>sequences : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
