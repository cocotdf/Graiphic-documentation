<h1>Memory Control Resume</h1>

<table>
  <tbody>
    <tr>
      <td valign="top" width="50%"><p align="center"><img src="assets/folder_memory_control.png" alt="folder_memory_control" width="260" /></p></td>
      <td valign="top" width="50%"><p align="center"><img src="assets/memory_control_menu.png" alt="memory_control_menu" width="260" /></p></td>
    </tr>
  </tbody>
</table>

<p>In this section you’ll find a list of all memory control fonctionalities.</p>

|  | **ICONS** | **DESCRIPTION** |
| --- | --- | --- |
| [Create Tensor](../create-tensor/README.md) | ![Create_Tensor.Png](/_assets/shared-images/bf/bf516ea843ae-create_tensor.png) | Allocates size bytes of linear memory on the device and returns a tensor to the allocated memory. |
| [Create Tensor & Host To Device](../create-tensor-host-to-device/README.md) | ![Create_Tensor_And_Host_To_Device.Png](/_assets/shared-images/d8/d89c87163d1c-create_tensor_and_host_to_device.png) | Allocates size bytes of linear memory on the device and copies data between host and device. Returns a tensor to the allocated memory. |
| [Free Memory](../free-memory/README.md) | ![Free_Memory.Png](/_assets/shared-images/b2/b28731842d6a-free_memory.png) | Releases the memory space indicated by the tensor, which must have been returned by the “[Create Tensor](../create-tensor/README.md)” or “[Create Tensor & Host To Device](../create-tensor-host-to-device/README.md)” function call. |
| [Set Tensor](../set-tensor/README.md) | ![Set_Tensor.Png](/_assets/shared-images/ac/aceca2debbdc-set_tensor.png) | Initializes the tensor with the given value. |
| [Get Tensor Information](../get-tensor-information/README.md) | ![Get_Tensor_Information 1.Png](/_assets/shared-images/a7/a7767adfcc90-get_tensor_information-1.png) | Information of the tensor. |
| [Get Memory Status](../../../_unmigrated/perrine-graiphic-io/get-memory-status/README.md) | ![Get_Memory_Status.Png](assets/get_memory_status.png) | Gets free, total and used device memory. |
| [Copy Tensor](../copy-tensor-2/README.md) | ![Copy Tensor.Png](/_assets/shared-images/24/246c9ecdc85b-copy-tensor.png) | Copy the source tensor in tensor destination. |
| [Set Device](../set-device/README.md) | ![Set_Device.Png](/_assets/shared-images/b6/b649626f6c69-set_device.png) | Set device to be used for GPU executions. |
| [Reset Device](../reset-device/README.md) | ![Reset_Device.Png](/_assets/shared-images/bd/bd69a21ce4aa-reset_device.png) | Explicitly destroys and cleans up all resources associated with the current device in the current process. |
| [Host To Device](../host-to-device/README.md) | ![Host_To_Device.Png](/_assets/shared-images/25/25f00e7c4564-host_to_device.png) | Copies data between host and device. |
| [Device To Device](../device-to-device/README.md) | ![Device_To_Device.Png](/_assets/shared-images/b9/b97c85747c6c-device_to_device.png) | Copies data between device and device. |
| [Device To Host](../device-to-host/README.md) | ![Device_To_Host.Png](/_assets/shared-images/40/40b24b88f215-device_to_host.png) | Copies data between device and host. |
| [Device To Host & Free](../device-to-host-free/README.md) | ![Device_To_Host_And_Free.Png](/_assets/shared-images/9d/9db4430575bb-device_to_host_and_free.png) | Copies data between device and host and free the tensor on the device. |
