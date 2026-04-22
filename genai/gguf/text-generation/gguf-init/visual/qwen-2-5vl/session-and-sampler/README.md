<h1>Session And Sampler</h1>

<h2>Description</h2>

<p>Initialize a session and its sampler Type : polymorphic.</p>

<p align="center"><img src="assets/session-and-sampler.png" alt="Session And Sampler" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Session Parameters" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>Session Parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Model File Path" src="/_assets/shared-images/09/0971eb44b0da-cpath.png" width="42"/></td>
      <td valign="top"><strong>Model File Path : <em>path</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="MMProj File Path" src="/_assets/shared-images/09/0971eb44b0da-cpath.png" width="42"/></td>
      <td valign="top"><strong>MMProj File Path : <em>path</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="n cpu threads" src="/_assets/shared-images/e6/e64a060992b9-ci32.png" width="42"/></td>
      <td valign="top"><strong>n cpu threads : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="nb gpu layers" src="/_assets/shared-images/e6/e64a060992b9-ci32.png" width="42"/></td>
      <td valign="top"><strong>nb gpu layers : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="n_ctx" src="/_assets/shared-images/e6/e64a060992b9-ci32.png" width="42"/></td>
      <td valign="top"><strong>n_ctx : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="system prompt" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>system prompt : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="always keep system prompt" src="/_assets/shared-images/06/06612771a6c0-cbool.png" width="42"/></td>
      <td valign="top"><strong>always keep system prompt : <em>boolean</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="Session Parameters" src="assets/Session Parameters.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Sampler Parameters" src="/_assets/shared-images/ba/ba242cb839de-cnclst.png" width="32"/> <strong>Sampler Parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="temperature" src="/_assets/shared-images/8c/8c54522fc255-csgl.png" width="42"/></td>
      <td valign="top"><strong>temperature : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="top_p" src="/_assets/shared-images/8c/8c54522fc255-csgl.png" width="42"/></td>
      <td valign="top"><strong>top_p : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="min_p" src="/_assets/shared-images/8c/8c54522fc255-csgl.png" width="42"/></td>
      <td valign="top"><strong>min_p : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="top_k" src="/_assets/shared-images/e6/e64a060992b9-ci32.png" width="42"/></td>
      <td valign="top"><strong>top_k : <em>integer</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="Sampler Parameters" src="/_assets/shared-images/28/289b90d639f2-sampler-parameters.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Qwen25VL out" src="/_assets/shared-images/c3/c3a2279ef770-iqwen25vllvclass.png" width="42"/></td>
      <td valign="top"><strong>Qwen25VL out : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
